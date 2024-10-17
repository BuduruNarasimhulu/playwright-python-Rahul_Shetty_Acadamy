import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_get():
    async with async_playwright() as playwright:
        context = await playwright.request.new_context()
        response = await context.get(url="https://mocki.io/v1/5aa8c16f-db9e-4efc-8cba-91f4841c491d")
        print(response)
        assert response.status == 200
        assert response.status_text == 'OK'
        assert response.headers["content-type"] == "application/json"
        res = await response.json()
        size = len(res)
        print(size)
        print(res)

pytest.main([__file__])





