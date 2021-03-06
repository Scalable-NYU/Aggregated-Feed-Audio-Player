from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter

from api import get_entry
import time

app = Flask(__name__)
app.secret_key = "supersecret"
blueprint = make_twitter_blueprint(
    api_key="GNTPJ8alh2T4wC6396QB1qLao",
    api_secret="5mGnp5fHYea9nf57aiPhOR04wD1oUOJSAsP9rcYQCD2KilvPJn",
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/")
def index():
    if not twitter.authorized:
        return redirect(url_for("twitter.login"))
    resp = twitter.get("account/settings.json")
    stream_entries = get_stream()
    return render_template("index.html", entries = stream_entries)

@app.route("/logout")
def logout():
    return redirect(url_for("twitter.login"))

@app.route("/twitter")
def twitter_profile():
    resp = twitter.get("account/settings.json")
    print(resp.json()["screen_name"])
    return redirect("https://twitter.com/@" + resp.json()["screen_name"])

@app.route("/notion")
def notion():
    return redirect("https://www.notion.so/cloudcomputingproject/Final-Presentation-Stuff-646a903c3f8b456f98d842b8224d55df")

def get_stream():
    usr_id = "andy"
    entries = get_entry(usr_id)

    return entries


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 80)
