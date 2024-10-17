import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_google_page_navigation():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()

        # Create a new page in the context
        page = await context.new_page()
        await page.goto("https://www.google.com/")

        await page.fill("//textarea[@id='APjFqb']", "Python")

        await page.press("//textarea[@id='APjFqb']", "Enter")

        await page.click('//h3[@class="LC20lb MBeuO DKV0Md"]')
        await page.wait_for_timeout(3000)
        await context.close()
        await browser.close()

@pytest.mark.asyncio
async def test_wrapper():
    await test_google_page_navigation()

pytest.main([__file__])
