# POC Scraper Pipeline

## Prerequisites

- Node.js & npm (for `stagehand`)
- Python 3.9+
- `pip install playwright` and `playwright install`
- (Optionally) `npm install -g @browserbase/stagehand`

## Steps

### 1. `Record`  
   ```bash
   npx @browserbase/stagehand record --format json --output session.json "https://passport.appf.io/sign_in?idp_type=tportal&vhostless=true"
````

### 2. `Convert`

```bash
python convert_session.py session.json BILT_APPFOLIO_FETCH_BALANCE AppfolioFetchBalanceScraper fetch_balance scrapers/appfolio_fetch_balance.py
```

### 3. `Run`

```bash
python runner.py
```