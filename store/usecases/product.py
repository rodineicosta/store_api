from typing import List
from uuid import UUID

import pymongo
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from store.core.exceptions import InsertionException, NotFoundException
from store.db.mongo import db_client
from store.models.product import ProductModel
from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut


class ProductUsecase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        product_model = ProductModel(**body.model_dump())
        try:
            await self.collection.insert_one(product_model.model_dump())
        except Exception as exc:
            raise InsertionException(message=f"Error inserting product: {str(exc)}")

        return ProductOut(**product_model.model_dump())

    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})

        if not result:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        return ProductOut(**result)

    async def query(
        self, min_price: float = None, max_price: float = None
    ) -> List[ProductOut]:
        filter_dict = {}

        if min_price is not None or max_price is not None:
            from bson import Decimal128

            price_filter = {}
            if min_price is not None:
                price_filter["$gt"] = Decimal128(str(min_price))
            if max_price is not None:
                price_filter["$lt"] = Decimal128(str(max_price))
            filter_dict["price"] = price_filter

        return [ProductOut(**item) async for item in self.collection.find(filter_dict)]

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        existing_product = await self.collection.find_one({"id": id})
        if not existing_product:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        from datetime import datetime, timezone

        update_data = body.model_dump(exclude_none=True)
        update_data["updated_at"] = datetime.now(timezone.utc)

        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": update_data},
            return_document=pymongo.ReturnDocument.AFTER,
        )

        return ProductUpdateOut(**result)

    async def delete(self, id: UUID) -> bool:
        product = await self.collection.find_one({"id": id})
        if not product:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        result = await self.collection.delete_one({"id": id})

        return True if result.deleted_count > 0 else False


product_usecase = ProductUsecase()
