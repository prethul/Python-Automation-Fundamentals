from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    print("processing")
    page.goto("https://www.youtube.com/",wait_until="networkidle")

    html = page.content()

    with open("index.html","w",encoding="utf-8") as f:
        f.write(html)

    print("Done")
