import time
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_tiktok_video_links(username, max_attempts=10, scroll_pause=5):
    """Extracts all video links from a TikTok profile by scrolling down until no new videos load."""

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    # Set up WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = f"https://www.tiktok.com/@{username}"
    driver.get(url)
    time.sleep(5)  # Allow initial page load

    video_links = set()
    last_video_count = 0
    attempts = 0

    while attempts < max_attempts:
        # Find all video elements
        video_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/video/')]")

        for elem in video_elements:
            video_links.add(elem.get_attribute("href"))

        print(f"Attempt {attempts + 1}: Found {len(video_links)} videos so far...")

        # Stop if no new videos are loaded
        if len(video_links) == last_video_count:
            print("No new videos found. Stopping scroll.")
            break

        last_video_count = len(video_links)

        # Scroll down using JavaScript
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause)  # Pause to let new content load

        attempts += 1

    driver.quit()  # Close the browser
    return list(video_links)


def save_links_to_csv(links, filename="tiktok_links.csv"):
    """Saves video links to a CSV file."""
    df = pd.DataFrame(links, columns=["TikTok Video Links"])
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"Saved {len(links)} links to {filename}")


if __name__ == "__main__":
    username = "markus.soeder"
    video_links = get_tiktok_video_links(username, max_attempts=30, scroll_pause=5)

    if video_links:
        save_links_to_csv(video_links)
    else:
        print("No video links found or profile is private.")
