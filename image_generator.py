
from PIL import Image, ImageDraw, ImageFont
import os


def generate_job_card(job):

    width = 1000
    height = 500

    img = Image.new("RGB", (width, height), color=(18, 18, 18))
    draw = ImageDraw.Draw(img)

    try:
        title_font = ImageFont.truetype("Arial.ttf", 60)
        text_font = ImageFont.truetype("Arial.ttf", 40)
    except:
        title_font = None
        text_font = None

    company = job.get("company", "Unknown Company")
    title = job.get("title", "Job Opening")

    draw.text((80, 120), "NEW TECH JOB", fill=(0, 180, 255), font=title_font)

    draw.text((80, 220), company, fill=(255, 255, 255), font=text_font)

    draw.text((80, 300), title, fill=(200, 200, 200), font=text_font)

    filename = "job_card.png"

    # save image
    img.save(filename)

    # return absolute path
    return os.path.abspath(filename)

