from playwright.sync_api import sync_playwright
# from pixelmatch import pixelmatch


def get_url_screenshot(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, wait_until='networkidle')
        screenshot = page.screenshot()
        browser.close()
        print(type(screenshot))
        return screenshot


# def get_num_diff_pixels(img1, img2):
#     # TODO: convert byte img to d1 array
#     # TODO: calculate diff
#     diff = []
#     num_diff_pixels = pixelmatch(img1, img2, 1280, 720, diff, threshold=0.1)
#     print(num_diff_pixels)
#     return num_diff_pixels
