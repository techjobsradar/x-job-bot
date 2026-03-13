
def generate_tweet(job):

    company = job.get("company", "Unknown Company")
    title = job.get("title", "Job Opening")
    link = job.get("link", "")

    tweet = f"""
New Remote Job!

Company: {company}
Role: {title}

Apply here:
{link}

#RemoteJobs #TechJobs #Hiring
"""

    # remove problematic unicode characters
    tweet = tweet.encode("utf-8", "ignore").decode("utf-8")

    return tweet.strip()
