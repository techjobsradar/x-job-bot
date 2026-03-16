import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def post_tweet(driver, tweet, image_path):

    driver.get("https://x.com/home")

    wait = WebDriverWait(driver, 25)

    # ----------------------------
    # TWEET TEXT AREA
    # ----------------------------
    tweet_box = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div[data-testid="tweetTextarea_0"]')
        )
    )

    tweet_box.click()

    # type slowly (avoids X bot detection)
    for ch in tweet:
        tweet_box.send_keys(ch)
        time.sleep(0.02)

    time.sleep(2)

    # ----------------------------
    # UPLOAD IMAGE
    # ----------------------------
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

    # Wait for image preview to load
    time.sleep(8)

    # ----------------------------
    # POST BUTTON
    # ----------------------------
    
    post_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[data-testid="tweetButtonInline"]')
        )
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", post_button)

    time.sleep(2)

    driver.execute_script("arguments[0].click();", post_button)

    driver.execute_script("arguments[0].scrollIntoView(true);", post_button)

    time.sleep(2)

    try:
        post_button.click()
    except:
        driver.execute_script("arguments[0].click();", post_button)

    print("Tweet posted successfully")

    time.sleep(6)