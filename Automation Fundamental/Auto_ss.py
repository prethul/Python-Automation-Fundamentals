from playwright.sync_api import sync_playwright

with sync_playwright() as p :

    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    print("Processing...")
    page.goto("https://www.github.com/",wait_until="networkidle")

    #screenshot
    #page.screenshot(path="screenshot.png",full_page=True)

    # screenshot to pdf making..
    page.pdf(path="page.pdf", format="A4" , print_background=True)

    print("Finished...")
    browser.close()

