
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from image_generator import generate_job_card


def post_tweet(driver, tweet, job):

    driver.get("https://x.com/compose/post")

    wait = WebDriverWait(driver, 20)

    tweet_box = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="textbox"]'))
    )

    tweet_box.click()

    # type tweet slowly
    for ch in tweet:
        tweet_box.send_keys(ch)

    # generate job card image
    image_path = generate_job_card(job)

    # upload image
    upload_input = wait.until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))
    )

    upload_input.send_keys(image_path)

    time.sleep(4)

    # wait for post button
    post_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="tweetButton"]'))
    )

    # scroll into view
    driver.execute_script("arguments[0].scrollIntoView(true);", post_button)

    time.sleep(2)

    # click with JS to avoid overlay blocking
    driver.execute_script("arguments[0].click();", post_button)

    print("Tweet posted successfully")

    time.sleep(5)
