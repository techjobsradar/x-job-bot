def filter_jobs(jobs):
    """
    Remove duplicate or invalid jobs
    """
    filtered = []
    seen = set()

    for job in jobs:
        title = job.get("title", "").strip()

        if title and title not in seen:
            seen.add(title)
            filtered.append(job)

    return filtered