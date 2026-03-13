
import requests
from bs4 import BeautifulSoup


def collect_jobs():

    jobs = []

    url = "https://weworkremotely.com/remote-jobs.rss"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "xml")

    items = soup.find_all("item")

    for item in items[:10]:

        title_text = item.title.text
        link = item.link.text

        # Example title format:
        # "Company: Job Title"

        if ":" in title_text:
            company, title = title_text.split(":", 1)
        else:
            company = "Unknown"
            title = title_text

        job = {
            "company": company.strip(),
            "title": title.strip(),
            "link": link
        }

        jobs.append(job)

    return jobs

