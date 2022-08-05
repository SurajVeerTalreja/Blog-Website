from flask import Flask, render_template
import requests
from datetime import datetime
import os

FORM_API_TOKEN = os.environ.get("FORM_API")

app = Flask(__name__)

today = datetime.now()
today = today.strftime("%B %d %Y")
blog_url = "https://api.npoint.io/1617f8c67c773e8f27f8"

blog_response = requests.get(blog_url)
all_blogs = blog_response.json()


@app.route("/")
def home_page():
    return render_template("index.html", complete_blogs=all_blogs, date=today)


@app.route("/About")
def about_me():
    return render_template("about.html")


@app.route("/Contact")
def contact_me():
    return render_template("contact.html", api=FORM_API_TOKEN)


@app.route("/post/<int:blog_id>")
def blog_post(blog_id):
    if blog_id == 1:
        return render_template("post.html", blogs=all_blogs, date=today, id=blog_id, background_pic='/static/assets/img/cacti.jpg')
    elif blog_id == 2:
        return render_template("post.html", blogs=all_blogs, date=today, id=blog_id, background_pic='/static/assets/img/dog.jpg')
    else:
        return render_template("post.html", blogs=all_blogs, date=today, id=blog_id, background_pic='/static/assets/img/fasting.jpg')


if __name__ == "__main__":
    app.run(debug=True)
