import pytest
from playwright.async_api import async_playwright,expect

@pytest.mark.asyncio
async def test_login_page_error_message():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        # URL
        await page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        # Username text box
        await page.fill("//input[@id='username']", "")
        # Password text box
        await page.fill("//input[@id='password']", "12345")
        # Login button
        await page.click("//input[@id='signInBtn']")
        # Wait for the error message
        error_message = page.locator("//div[@class='alert alert-danger col-md-12']")
        await expect(error_message).to_be_visible()
        # Error message checking
        if await error_message.is_visible():
            print("Empty username/password.", await error_message.is_visible())
        else:
            print("No Text")
        # Close
        await browser.close()

pytest.main([__file__])

