import asyncio
import httpx
import pytest


async def fetch_products():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NmZmMjdlOGFlMmFmZDRjMGI4ZTUxMzEiLCJ1c2VyRW1haWwiOiJuYXJhc2ltaHVsdWJ1ZHVydTQ4MjJAZ21haWwuY29tIiwidXNlck1vYmlsZSI6NjMwMzc1OTE5NywidXNlclJvbGUiOiJjdXN0b21lciIsImlhdCI6MTcyODQ1MjIzOSwiZXhwIjoxNzYwMDA5ODM5fQ.jBE8eZr55qSUv-imqa5B5Cqt3IWnZmYXlvvh7qXIoFk"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://rahulshettyacademy.com/api/ecom/product/get-all-products",
            headers=headers
        )

    api_response = response.json()

    # Check for session timeout
    if api_response.get('message') == 'Session Timeout':
        raise Exception("Session Timeout. Please check your token.")

    return api_response.get("data", []), api_response.get("count")


# Test Cases
@pytest.mark.asyncio
async def test_product_count():
    products, expected_count = await fetch_products()
    assert expected_count == len(products), "Product count does not match the number of products."


@pytest.mark.asyncio
async def test_product_data():
    products, _ = await fetch_products()
    for product in products:
        assert all(key in product for key in ["_id", "productName", "productCategory", "productSubCategory",
                                              "productPrice", "productDescription", "productImage",
                                              "productRating", "productTotalOrders", "productStatus",
                                              "productFor", "productAddedBy", "__v"]), "Missing product keys."
        assert isinstance(product["_id"], str)
        assert isinstance(product["productName"], str)
        assert isinstance(product["productCategory"], str)
        assert isinstance(product["productSubCategory"], str)
        assert isinstance(product["productPrice"], int)
        assert isinstance(product["productDescription"], str)
        assert isinstance(product["productImage"], str)
        assert isinstance(product["productRating"], str)
        assert isinstance(product["productTotalOrders"], str)
        assert isinstance(product["productStatus"], bool)
        assert isinstance(product["productFor"], str)
        assert isinstance(product["productAddedBy"], str)
        assert isinstance(product["__v"], int)


@pytest.mark.asyncio
async def test_product_categories():
    products, _ = await fetch_products()
    valid_categories = {
        "fashion": ["shirts", "pants", "dresses"],
        "household": ["shoes", "furniture", "appliances"],
        "electronics": ["mobiles", "laptops", "accessories"]
    }

    for product in products:
        category = product["productCategory"]
        subcategory = product["productSubCategory"]
        assert category in valid_categories, "Invalid Product Category."
        assert subcategory in valid_categories[category], f"Invalid {category.capitalize()} SubCategory."


@pytest.mark.asyncio
async def test_product_price():
    products, _ = await fetch_products()
    for product in products:
        assert product["productPrice"] > 0, "Product Price should be positive."


@pytest.mark.asyncio
async def test_image_url():
    products, _ = await fetch_products()
    for product in products:
        assert product["productImage"].startswith("https://"), "Product Image URL should start with 'https://'."


@pytest.mark.asyncio
async def test_product_status():
    products, _ = await fetch_products()
    for product in products:
        assert isinstance(product["productStatus"], bool), "Product Status should be a boolean."


@pytest.mark.asyncio
async def test_total_orders():
    products, _ = await fetch_products()
    for product in products:
        assert int(product["productTotalOrders"]) >= 0, "Product Total Orders should be non-negative."


# Run Tests
if __name__ == "__main__":
    asyncio.run(pytest.main())

