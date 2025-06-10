def test_open_google(page):
    page.goto("https://www.google.com")
    assert "Google" in page.title()

from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://realpython.github.io/fake-jobs/')
        context = page.context
        with context.expect_page() as new_page_info:
            page.click("(//a[.='Learn'])[1]")
        new_page = new_page_info.value
        print(f"New page url {new_page.url}")
        print(f"Old page url {page.url}")
        new_page.click("//a[.='Join']")
        time.sleep(3)
        browser.close()

run()