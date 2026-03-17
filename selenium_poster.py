import time
import os
import json
import base64
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def load_cookies(driver):
    cookies_b64 = os.environ.get("TWITTER_COOKIES")
    if not cookies_b64:
        raise Exception("TWITTER_COOKIES secret not set")
    cookies = json.loads(base64.b64decode(cookies_b64).decode("utf-8"))
    driver.get("https://x.com")
    time.sleep(5)
    for cookie in cookies:
        cookie.pop("sameSite", None)
        cookie.pop("storeId", None)
        cookie.pop("hostOnly", None)
        cookie.pop("session", None)
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"Skipping cookie: {e}")
    driver.get("https://x.com/home")
    time.sleep(8)
    driver.save_screenshot("screenshot_after_login.png")
    print("Current URL:", driver.current_url)
    print("Page title:", driver.title)
    # Check if actually logged in
    if "login" in driver.current_url.lower() or "flow" in driver.current_url.lower():
        raise Exception("Not logged in - cookies failed. URL: " + driver.current_url)

def post_tweet(driver, tweet, image_path):
    load_cookies(driver)
    wait = WebDriverWait(driver, 30)

    print("Looking for tweet box...")
    tweet_box = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div[data-testid="tweetTextarea_0"]')
        )
    )
    print("Tweet box found!")
    tweet_box.click()
    time.sleep(1)
    for ch in tweet:
        tweet_box.send_keys(ch)
        time.sleep(0.02)
    time.sleep(2)

    upload_input = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//input[@type="file"]')
        )
    )
    print("Uploading Image:", image_path)
    if not os.path.exists(image_path):
        print("Image not found:", image_path)
        return
    upload_input.send_keys(image_path)
    time.sleep(8)

    print("Looking for post button...")
    post_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[data-testid="tweetButtonInline"]')
        )
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", post_button)
    time.sleep(2)
    driver.execute_script("arguments[0].click();", post_button)
    time.sleep(5)
    driver.save_screenshot("screenshot_after_post.png")
    print("Current URL after post:", driver.current_url)
    print("Tweet posted successfully")
