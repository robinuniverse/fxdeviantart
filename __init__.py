from flask import Flask, render_template
from urllib.parse import quote
from urllib.request import urlopen
import json

# Manually get data from the deviantArt oembed API to build a better and more reliable embed
# Robin Universe w/ tweaks from Dania
# 05 . 04 . 22

# Initialise Flask
app = Flask(__name__)

# Open config.json and load it into a dictionary variable
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Main Function
@app.route("/<path:subpath>")
def fxdeviantart(subpath):
    # Original link to submission, to be used for the `url` parameter in the template
    origin = "https://deviantart.com/" + subpath

    # Get the submission's JSON data
    data = json.load(
        urlopen(("https://backend.deviantart.com/oembed?url=" + str(quote(origin))))
    )

    # Return the template with the data
    return render_template(
        "index.html",
        user="by " + data["author_name"],
        img=data["url"],
        url=origin,
        title=data["title"],
        site_name=config["siteConfig"]["siteName"],
        color=config["siteConfig"]["embedColor"],
    )