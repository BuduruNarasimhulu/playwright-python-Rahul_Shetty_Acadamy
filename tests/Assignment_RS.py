import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_Registration_and_login_page():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()

        # Registration Page
        page = await context.new_page()
        await page.goto("https://rahulshettyacademy.com/client/")
        await page.wait_for_selector("//p[@class='login-wrapper-footer-text']")
        await page.click("//p[@class='login-wrapper-footer-text']")

        # Wait for the input fields to be visible before filling them
        await page.wait_for_selector("//input[@id='firstName']")
        await page.fill("//input[@id='firstName']", "Narasimhulu")
        await page.fill("//input[@id='lastName']", "Buduru")
        await page.fill("//input[@id='userEmail']", "narasimhulubuduru4822@gmail.com")
        await page.fill("//input[@id='userMobile']", "6303759197")
        await page.select_option("//select[@class='custom-select ng-untouched ng-pristine ng-valid']", "Engineer")
        await page.check("input[value='Male']")
        await page.fill("//input[@id='userPassword']", "Narasimhulu@12")
        await page.fill("//input[@id='confirmPassword']", "Narasimhulu@12")
        await page.click("//input[@type='checkbox']")
        await page.wait_for_selector("//input[@id='login']")
        await page.click("//input[@id='login']")
        await page.wait_for_timeout(3000)

        # Login Page (using the same context and page)
        await page.goto("https://rahulshettyacademy.com/client")
        await page.fill("//input[@id='userEmail']", "narasimhulubuduru4822@gmail.com")
        await page.fill("//input[@id='userPassword']", "Narasimhulu@12")
        await page.click("//input[@id='login']")
        await page.wait_for_selector("//div[@class='container']//div[1]//div[1]//div[1]//button[2]")
        await page.click("//div[@class='container']//div[1]//div[1]//div[1]//button[2]")
        await page.wait_for_timeout(3000)

        await context.close()
        await browser.close()

pytest.main([__file__])


