from playwright.async_api import async_playwright
import asyncio


async def login_api():
    async with async_playwright() as playwright:
        payload = {
            "userEmail": "narasimhulubuduru4822@gmail.com",
            "userPassword": "",
        }
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        response = await page.request.post("https://rahulshettyacademy.com/api/ecom/auth/login", data=payload)

        if response.status != 200:
            print((await response.json()).get('message'))
        else:
            print((await response.json()).get('message'))


# Run the async function
if __name__ == "__main__":
    asyncio.run(login_api())



