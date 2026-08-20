from playwright.sync_api import sync_playwright
import os
import time

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1200, "height": 460})
        file_url = f"file:///{os.path.abspath('banner-generator.html').replace(os.sep, '/')}"
        page.goto(file_url, wait_until="networkidle")
        
        # Wait a bit for external fonts and CSS to fully apply, and for the canvas particles to draw
        time.sleep(2)
        
        # The banner container is #bannerContainer
        banner_element = page.query_selector("#bannerContainer")
        if banner_element:
            banner_element.screenshot(path="masud_rana_github_banner.png")
            print("Screenshot taken successfully of the banner container.")
        else:
            page.screenshot(path="masud_rana_github_banner.png")
            print("Banner container not found. Fallback: took screenshot of the whole page.")
            
        browser.close()

if __name__ == "__main__":
    main()
