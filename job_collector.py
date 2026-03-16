import feedparser


# --------------------------------
# RSS FEEDS (ALL SOURCES)
# --------------------------------

RSS_FEEDS = [

    # ENTRY LEVEL
    "https://www.indeed.co.in/rss?q=entry+level+software+engineer",
    "https://www.indeed.co.in/rss?q=junior+developer",
    "https://www.indeed.co.in/rss?q=graduate+software+engineer",
    "https://www.indeed.co.in/rss?q=software+engineer+intern",

    # MID LEVEL
    "https://www.indeed.co.in/rss?q=software+engineer",
    "https://www.indeed.co.in/rss?q=devops+engineer",
    "https://www.indeed.co.in/rss?q=cloud+engineer",
    "https://www.indeed.co.in/rss?q=site+reliability+engineer",

    # SENIOR
    "https://www.indeed.co.in/rss?q=senior+software+engineer",
    "https://www.indeed.co.in/rss?q=senior+devops+engineer",
    "https://www.indeed.co.in/rss?q=senior+cloud+engineer",

    # MANAGEMENT
    "https://www.indeed.co.in/rss?q=engineering+manager",
    "https://www.indeed.co.in/rss?q=tech+lead",

    # DIRECTOR
    "https://www.indeed.co.in/rss?q=director+engineering",
    "https://www.indeed.co.in/rss?q=director+software",

    # REMOTE JOB BOARDS
    "https://weworkremotely.com/categories/remote-programming-jobs.rss",
    "https://remoteok.com/remote-dev-jobs.rss",

    # STARTUP JOBS
    "https://www.ycombinator.com/jobs/rss"
]


# --------------------------------
# INDIA LOCATIONS
# --------------------------------

INDIA_LOCATIONS = [
    "india","bangalore","bengaluru","hyderabad","chennai",
    "pune","mumbai","delhi","gurgaon","noida","kolkata",
    "ahmedabad","remote"
]


# --------------------------------
# LOCATION DETECTION
# --------------------------------

def extract_location(text):

    text = text.lower()

    for city in INDIA_LOCATIONS:
        if city in text:
            return city.title()

    return "India"


# --------------------------------
# COMPANY DETECTION
# --------------------------------

def extract_company(entry):

    if "author" in entry:
        return entry.author

    if "company" in entry:
        return entry.company

    if "title" in entry and " at " in entry.title.lower():
        parts = entry.title.split(" at ")
        if len(parts) > 1:
            return parts[1]

    return "Company"


# --------------------------------
# COLLECT JOBS
# --------------------------------

def collect_jobs():

    jobs = []
    seen_links = set()

    for feed in RSS_FEEDS:

        print(f"\nFetching feed: {feed}")

        parsed = feedparser.parse(feed)

        print("Entries found:", len(parsed.entries))

        for entry in parsed.entries:

            title = entry.get("title", "")
            link = entry.get("link", "")
            summary = entry.get("summary", "")

            if not title or not link:
                continue

            if link in seen_links:
                continue

            seen_links.add(link)

            location = extract_location(summary)
            company = extract_company(entry)

            job = {
                "title": title,
                "company": company,
                "location": location,
                "link": link,
                "summary": summary
                
            }

            jobs.append(job)

    print(f"\nTotal jobs collected: {len(jobs)}")

    return jobs