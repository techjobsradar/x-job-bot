import time
import random
import os

from job_collector import collect_jobs
from job_filter import filter_jobs
from tweet_generator import generate_tweet
from image_generator import generate_job_card
from selenium_poster import post_tweet

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


POSTED_FILE = "posted_jobs.txt"
PROFILE_PATH = "selenium-profile"


# ---------------------------
# LOAD POSTED JOBS
# ---------------------------

def load_posted():

    if not os.path.exists(POSTED_FILE):
        # create file if not exists
        open(POSTED_FILE, "w").close()
        return set()

    with open(POSTED_FILE, "r") as f:
        return set(line.strip() for line in f if line.strip())


# ---------------------------
# SAVE POSTED JOB
# ---------------------------

def save_posted(link):

    link = link.strip()

    posted = load_posted()

    if link not in posted:
        with open(POSTED_FILE, "a") as f:
            f.write(link + "\n")

# ---------------------------
# START BROWSER
# ---------------------------

def start_driver():

    chrome_options = Options()

    chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

    chrome_options.add_argument(f"--user-data-dir={PROFILE_PATH}")

    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver


# ---------------------------
# MAIN BOT
# ---------------------------

def run_bot():

    print("🚀 Starting TechJobsRadar Bot")

    posted_jobs = load_posted()

    print("Collecting jobs...")

    jobs = collect_jobs()

    jobs = filter_jobs(jobs)

    print("Jobs collected:", len(jobs))

    job_to_post = None

for job in jobs:

    link = job.get("link")

    if not link:
        continue

    link = link.strip()

    if link not in posted_jobs:
        job_to_post = job
        break


    if not job_to_post:

        print("No new jobs found")
        return


    title = job_to_post["title"]

    print("Posting job:", title)


    tweet = generate_tweet(job_to_post)

    image_path = generate_job_card(job_to_post)


    driver = start_driver()

    try:

        post_tweet(driver, tweet, image_path)

        save_posted(job_to_post["link"])

        posted_jobs.add(job_to_post["link"])

        print("✅ Job posted successfully")


    except Exception as e:

        print("❌ Posting failed:", e)

    finally:

        driver.quit()


    delay = random.randint(900, 1800)

    print("Sleeping", delay, "seconds")

    time.sleep(delay)


# ---------------------------
# RUN
# ---------------------------

if __name__ == "__main__":
    run_bot()
