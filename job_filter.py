# ---------------------------
# EXPERIENCE LEVEL KEYWORDS
# ---------------------------

ENTRY_LEVEL = [
    "intern",
    "trainee",
    "junior",
    "fresher",
    "associate"
]

MID_LEVEL = [
    "engineer",
    "developer",
    "analyst",
    "consultant",
    "administrator"
]

SENIOR_LEVEL = [
    "senior",
    "lead",
    "principal",
    "architect",
    "manager"
]

DIRECTOR_LEVEL = [
    "director",
    "head",
    "vp",
    "vice president",
    "cto",
    "chief"
]


# ---------------------------
# INDIA LOCATIONS
# ---------------------------

INDIA_LOCATIONS = [
    "india",
    "bangalore",
    "bengaluru",
    "hyderabad",
    "chennai",
    "pune",
    "mumbai",
    "delhi",
    "gurgaon",
    "noida",
    "kolkata",
    "ahmedabad",
    "remote india",
    "remote"
]


# ---------------------------
# FILTER JOBS
# ---------------------------

def filter_jobs(jobs):

    filtered = []

    for job in jobs:

        title = job.get("title", "").lower()
        location = job.get("location", "").lower()

        # Allow India jobs OR remote jobs
        if "india" in location or "remote" in location.lower():
            filtered.append(job)
            continue

        # If location missing, still allow tech roles
        tech_keywords = [
            "engineer",
            "developer",
            "devops",
            "cloud",
            "backend",
            "frontend",
            "software",
            "fullstack",
            "data"
        ]

        if any(keyword in title for keyword in tech_keywords):
            filtered.append(job)

    return filtered