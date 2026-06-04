from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    print("processing....")
    page = browser.new_page()
    page.goto("https://www.facebook.com/")
    page.wait_for_timeout(5000)
    print(page.title())

    browser.close()