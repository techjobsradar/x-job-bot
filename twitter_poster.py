import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def post_tweet(driver, text):

    driver.get("https://x.com/compose/post")
    time.sleep(6)

    tweet_box = driver.find_element(By.XPATH, "//div[@data-testid='tweetTextarea_0']")

    tweet_box.click()
    time.sleep(1)

    # Clear previous draft
    tweet_box.send_keys(Keys.COMMAND + "a")
    tweet_box.send_keys(Keys.DELETE)

    time.sleep(1)

    # Type tweet
    tweet_box.send_keys(text)

    time.sleep(3)

    post_button = driver.find_element(By.XPATH, "//div[@data-testid='tweetButtonInline']")

    if post_button.is_enabled():
        post_button.click()
        print("Tweet posted successfully")
        time.sleep(3)

        driver.get("https://x.com/home")
        time.sleep(5)

        return True

    else:
        print("Post button disabled")
        return False