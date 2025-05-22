
import asyncio
from playwright.async_api import async_playwright
from scrapers.appfolio_fetch_balance import AppfolioFetchBalanceScraper

async def main():
    creds = {"username": "benjaminkramer84@gmail.com", "password": "xZ6y.s8!UP97hr.3"}
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        scraper = AppfolioFetchBalanceScraper(page)
        balance = await scraper.fetch_balance(creds)
        print("Fetched Balance:", balance)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
