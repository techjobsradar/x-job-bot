def generate_tweet(job):

    title = job.get("title", "Job Opening")
    company = job.get("company", "")
    location = job.get("location", "")
    role = job.get("role", title)
    link = job.get("link", "")

    lines = [title, ""]

    # Add company only if available
    if company and company.strip():
        lines.append(f"Company: {company}")

    # Add location only if available
    if location and location.strip():
        lines.append(f"Location: {location}")

    # Role should always appear
    lines.append(f"Role: {role}")

    lines.append("")
    lines.append("Apply Here:")
    lines.append(link)
    lines.append("")
    lines.append("#IndiaJobs #ITJobs #TechJobs #HiringIndia #DevOpsJobs")

    return "\n".join(lines)