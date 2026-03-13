
import time
import random
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from job_collector import collect_jobs
from job_filter import filter_jobs
from tweet_generator import generate_tweet
from selenium_poster import post_tweet


POSTED_FILE = "posted_jobs.txt"
PROFILE_PATH = "/Users/madhukandelli/x-job-bot/selenium-profile"


# ---------------------------
# LOAD POSTED JOBS
# ---------------------------
def load_posted():
    if not os.path.exists(POSTED_FILE):
        return set()

    with open(POSTED_FILE, "r") as f:
        return set(line.strip() for line in f.readlines())


# ---------------------------
# SAVE POSTED JOB
# ---------------------------

def save_posted(link):
    with open("posted_jobs.txt", "a") as f:
        f.write(link + "\n")

# ---------------------------
# START CHROME DRIVER
# ---------------------------
def start_driver():

    chrome_options = Options()

    # Mac Chrome binary
    chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

    # Stability options
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-notifications")

    # Selenium profile
    chrome_options.add_argument(f"--user-data-dir={PROFILE_PATH}")

    chrome_options.add_argument("--start-maximized")

    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-automation"]
    )

    chrome_options.add_experimental_option(
        "useAutomationExtension", False
    )

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )

    return driver


# ---------------------------
# MAIN BOT
# ---------------------------
def run_bot():

    print("Starting Job Bot...")

    driver = start_driver()

    posted_jobs = load_posted()

    print("Collecting jobs...")

    jobs = collect_jobs()

    jobs = filter_jobs(jobs)

    print("Jobs found:", len(jobs))

    for job in jobs:

        title = job["title"]
        link =job["link"]
        if link in posted_jobs:
            print("Skipping duplicate:", title)
            continue

        tweet = generate_tweet(job)

        try:

            print("Posting:", title)

            post_tweet(driver, tweet, job)

            save_posted(link)

            print("Posted successfully")

            driver.quit()

        except Exception as e:

            print("Posting failed:", e)

        delay = random.randint(900, 1800)

        print("Sleeping", delay, "seconds")

        time.sleep(delay)


# ---------------------------
# RUN
# ---------------------------
if __name__ == "__main__":
    run_bot()