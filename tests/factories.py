def product_data():
    return {
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }


def products_data():
    return [
        {"name": "Iphone 11 Pro Max", "quantity": 20, "price": "4.500", "status": True},
        {"name": "Iphone 12 Pro Max", "quantity": 15, "price": "5.500", "status": True},
        {"name": "Iphone 13 Pro Max", "quantity": 5, "price": "6.500", "status": True},
        {"name": "Iphone 14 Pro Max", "quantity": 10, "price": "8.500", "status": True},
        {
            "name": "Iphone 15 Pro Max",
            "quantity": 3,
            "price": "10.500",
            "status": False,
        },
        {"name": "Samsung Galaxy S21", "quantity": 8, "price": "3.200", "status": True},
        {
            "name": "Samsung Galaxy S22",
            "quantity": 12,
            "price": "7.800",
            "status": True,
        },
        {"name": "Samsung Galaxy S23", "quantity": 6, "price": "9.200", "status": True},
    ]


def products_data_with_price_filter():
    """Produtos especificamente para testar filtro de preço (price > 5000 and price < 8000)"""
    return [
        {
            "name": "Produto Filtro 1",
            "quantity": 10,
            "price": "5.500",
            "status": True,
        },
        {
            "name": "Produto Filtro 2",
            "quantity": 5,
            "price": "6.500",
            "status": True,
        },
        {
            "name": "Produto Filtro 3",
            "quantity": 8,
            "price": "7.500",
            "status": True,
        },
        {
            "name": "Produto Barato",
            "quantity": 15,
            "price": "4.500",
            "status": True,
        },
        {
            "name": "Produto Caro",
            "quantity": 3,
            "price": "8.500",
            "status": True,
        },
    ]
