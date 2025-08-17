from bson.binary import UuidRepresentation
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient as PyMongoClient

from store.core.config import settings


class MongoClient:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(
            settings.DATABASE_URL, uuidRepresentation="standard"
        )

    def get(self) -> AsyncIOMotorClient:
        return self.client


db_client = MongoClient()
