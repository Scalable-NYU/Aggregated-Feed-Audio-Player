from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter

import get_my_tweets as tweets

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
    assert resp.ok
    return render_template("index.html")

@app.route("/logout")
def logout():
    return redirect(url_for("twitter.login"))

@app.route("/twitter")
def twitter_profile():
    resp = twitter.get("account/settings.json")
    return redirect("https://twitter.com/@" + resp.json()["screen_name"])

@app.route("/notion")
def notion():
    return redirect("https://www.notion.so/cloudcomputingproject/Final-Presentation-Stuff-646a903c3f8b456f98d842b8224d55df")

if __name__ == "__main__":
    app.run(debug = True)