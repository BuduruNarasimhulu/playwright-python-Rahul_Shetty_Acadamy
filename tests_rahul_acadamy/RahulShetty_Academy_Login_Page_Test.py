import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_login_page():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        await page.fill("//input[@id='username']", "rahulshettyacademy")
        await page.fill("//input[@id='password']", "learning")
        await page.click("//input[@id='signInBtn']")
        await page.wait_for_selector(".card-title a")
        all_carts = await page.locator(".card-title a").all_text_contents()
        print(all_carts)
        await page.wait_for_timeout(3000)
        await browser.close()

pytest.main([__file__])




