from playwright.sync_api import sync_playwright

with sync_playwright() as p :
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    #new page browser
    page.goto("https://www.youtube.com/")
    page.wait_for_timeout(5000)

    #new another page browse

    page.goto("https://www.github.com/")
    page.wait_for_timeout(5000)

    #new another page browse
    page.goto("https://www.facebook.com/")
    page.wait_for_timeout(5000)
    #facebook reload
    page.reload()
    page.wait_for_timeout(5000)

    # go back to github
    page.go_back()
    page.wait_for_timeout(5000)

    #go back to youtube
    page.go_back()
    page.wait_for_timeout(3000)

    #go forward to github
    page.go_forward()
    page.wait_for_timeout(2000)
    page.reload()