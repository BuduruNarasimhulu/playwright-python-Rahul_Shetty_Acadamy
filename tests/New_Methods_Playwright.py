import pytest
from playwright.async_api import async_playwright, expect

@pytest.mark.asyncio
async def test_login_page_different_methods():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False, slow_mo=2000)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://rahulshettyacademy.com/angularpractice/")
        await page.locator("form input[name=\"name\"]").fill("Narasimhulu")
        await page.locator("input[name=\"email\"]").click()
        await page.locator("input[name=\"email\"]").fill("narasimhulubuduru4822@gmail.com")
        await page.get_by_placeholder("Password").click()
        await page.get_by_placeholder("Password").fill("Narasimhulu@12")
        await page.get_by_label("Check me out if you Love").check()
        await page.get_by_text("Employed").click()
        await page.locator("input[name=\"bday\"]").fill("2001-07-25")
        await page.get_by_role("button", name="Submit").click()

        is_visible = await page.get_by_text("Success! The Form has been submitted successfully!.").is_visible()
        print(is_visible)

        await context.close()
        await browser.close()

@pytest.mark.asyncio
async def test_wrapper():
    await test_login_page_different_methods()

pytest.main([__file__])


