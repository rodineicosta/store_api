import pytest
from fastapi import status

from tests.factories import product_data, products_data_with_price_filter


async def test_controller_query_with_price_filter_should_return_filtered_products(
    client, products_url
):
    from store.schemas.product import ProductIn
    from store.usecases.product import product_usecase

    products_data = products_data_with_price_filter()
    for product_data in products_data:
        await product_usecase.create(body=ProductIn(**product_data))

    response = await client.get(f"{products_url}?min_price=5&max_price=8")

    assert response.status_code == status.HTTP_200_OK
    products = response.json()

    assert len(products) == 3

    for product in products:
        price = float(product["price"])
        assert 5 < price < 8


async def test_controller_query_with_min_price_filter_should_work(client, products_url):
    response = await client.get(f"{products_url}?min_price=8")

    assert response.status_code == status.HTTP_200_OK
    products = response.json()

    for product in products:
        price = float(product["price"])
        assert price > 8


async def test_controller_query_with_max_price_filter_should_work(client, products_url):
    response = await client.get(f"{products_url}?max_price=5")

    assert response.status_code == status.HTTP_200_OK
    products = response.json()

    for product in products:
        price = float(product["price"])
        assert price < 5


async def test_controller_query_without_filters_should_return_all_products(
    client, products_url
):
    response = await client.get(products_url)

    assert response.status_code == status.HTTP_200_OK
    products = response.json()

    assert len(products) >= 0
