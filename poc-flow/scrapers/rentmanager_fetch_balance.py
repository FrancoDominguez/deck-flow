from playwright.async_api import Page
from scraper_registry import ScraperRegistry

@ScraperRegistry.register("BILT_RENTMANAGER_FETCH_BALANCE")
class RentManagerFetchBalanceScraper:
    def __init__(self, page: Page):
        self.page = page

    async def fetch_balance(self, params: dict):
        await page.type("xpath=/html/body[1]/div[3]/div[1]/form[1]/div[1]/div[1]/div[3]/input[1]", params["username"], delay=100)
        await page.type("xpath=/html/body[1]/div[3]/div[1]/form[1]/div[1]/div[1]/div[4]/input[1]", params["username"], delay=100)
        await self.click_loop(page, "xpath=/html/body[1]/div[3]/div[1]/form[1]/div[1]/div[1]/div[7]/input[1]")
        result = await page.inner_text("None")
        return result.strip()
        result = await page.inner_text("None")
        return result.strip()
        result = await page.inner_text("None")
        return result.strip()
        result = await page.inner_text("None")
        return result.strip()
        result = await page.inner_text("None")
        return result.strip()
        result = await page.inner_text("None")
        return result.strip()
        result = await page.inner_text("None")
        return result.strip()
