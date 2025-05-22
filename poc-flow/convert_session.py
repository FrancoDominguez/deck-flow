import json
import argparse
from pathlib import Path

# Mapping Stagehand and Stagehand-Agent action types to Playwright-based Python snippets
action_map = {
    "goto": lambda act: f'        await page.goto("{act.get("url")}")',
    # 'act' from Stagehand-Agent: determine fill or click via playwrightArguments
    "act": lambda act: (
        f'        await page.type("{act["playwrightArguments"]["selector"]}", params["username"], delay=100)' 
        if act["playwrightArguments"]["method"] == "fill" else
        f'        await self.click_loop(page, "{act["playwrightArguments"]["selector"]}")'
    ),
    "click": lambda act: f'        await self.click_loop(page, "{act.get("selector")}")',
    "wait": lambda act: (
        f'        await page.wait_for_selector("{act.get("selector")}", timeout={act.get("parameters")})' 
        if act.get("selector") else
        f'        await page.wait_for_timeout({act.get("parameters")})'
    ),
    "extract": lambda act: (
        f'        result = await page.inner_text("{act.get("selector")}")' + "\n" +
        f'        return result.strip()'
    ),
    "navback": lambda act: '        await page.go_back()',
    "close": lambda act: '        await stagehand.close()'
}

CLASS_TEMPLATE = '''from playwright.async_api import Page
from scraper_registry import ScraperRegistry

@ScraperRegistry.register("{registry_key}")
class {class_name}:
    def __init__(self, page: Page):
        self.page = page

    async def {method_name}(self, params: dict):
{body}
'''

def generate_scraper(session_file: Path, registry_key: str, class_name: str, method_name: str, output_file: Path):
    # Load recorded actions
    actions = json.loads(session_file.read_text())
    lines = []
    for act in actions:
        # Skip screenshots
        if act.get("type") == "screenshot":
            continue
        mapper = action_map.get(act.get("type"))
        if mapper:
            try:
                lines.append(mapper(act))
            except Exception as e:
                lines.append(f'        # Error mapping action: {act}, error: {e}')
        else:
            lines.append(f'        # Skipped unknown action type: {act.get("type")}')
    body = "\n".join(lines)

    # Render class code
    code = CLASS_TEMPLATE.format(
        registry_key=registry_key,
        class_name=class_name,
        method_name=method_name,
        body=body
    )

    # Write to file
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(code)
    print(f"Generated scraper class at {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Python scraper from Stagehand session JSON.")
    parser.add_argument("session", type=Path, help="Path to session.json")
    parser.add_argument("registry_key", help="ScraperRegistry key, e.g. BILT_FETCH_BALANCE")
    parser.add_argument("class_name", help="Python class name for the scraper")
    parser.add_argument("method_name", help="Method name inside the class")
    parser.add_argument("output", type=Path, help="Output .py file path")
    args = parser.parse_args()
    generate_scraper(args.session, args.registry_key, args.class_name, args.method_name, args.output)
