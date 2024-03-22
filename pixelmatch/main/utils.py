from playwright.sync_api import sync_playwright


def get_url_screenshot(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, wait_until='networkidle')
        screenshot = page.screenshot()
        browser.close()
        return screenshot
