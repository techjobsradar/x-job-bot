import os
import uuid
import textwrap
from PIL import Image, ImageDraw, ImageFont

TEMPLATE = "poster_template.png"


def generate_job_card(job):

    # -------------------------
    # JOB DATA
    # -------------------------

    title = job.get("title", "Cloud Engineer")
    company = job.get("company", "Company")
    location = job.get("location", "Remote")
    link = job.get("link", "")

    # Limit title length so poster does not break
    title = title[:60]

    filename = f"job_card_{uuid.uuid4().hex}.png"

    template_path = os.path.abspath(TEMPLATE)

    img = Image.open(template_path).convert("RGB")

    draw = ImageDraw.Draw(img)

    width = img.width

    # -------------------------
    # FONT PATHS
    # -------------------------

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    FONT_DIR = os.path.join(BASE_DIR, "fonts")

    title_font = ImageFont.truetype(
        os.path.join(FONT_DIR, "Orbitron-Bold.ttf"), 80
    )

    text_font = ImageFont.truetype(
        os.path.join(FONT_DIR, "Poppins-Medium.ttf"), 44
    )

    link_font = ImageFont.truetype(
        os.path.join(FONT_DIR, "Poppins-Regular.ttf"), 34
    )

    # -------------------------
    # TITLE WRAPPING
    # -------------------------

    wrapped_title = textwrap.wrap(title.upper(), width=18)

    y = 260

    for line in wrapped_title:

        bbox = draw.textbbox((0, 0), line, font=title_font)

        w = bbox[2] - bbox[0]

        x = (width - w) / 2

        draw.text((x, y), line, fill="#7FE3FF", font=title_font)

        y += 85

    # -------------------------
    # JOB INFO
    # -------------------------

    draw.text((320, 560), f"Company: {company}", fill="white", font=text_font)

    draw.text((320, 620), f"Location: {location}", fill="white", font=text_font)

    # -------------------------
    # APPLY SECTION
    # -------------------------

    draw.text((320, 700), "Apply Now ↓", fill="#FFD166", font=text_font)

    short_link = link[:45]

    draw.text((320, 760), short_link, fill="white", font=link_font)

    # -------------------------
    # SAVE POSTER
    # -------------------------

    save_path = os.path.abspath(filename)

    img.save(save_path, format="PNG")

    print("Poster generated:", save_path)

    return save_path