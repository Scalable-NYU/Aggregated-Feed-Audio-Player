from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter

from subprocess import *

from api import get_entry

# To execute commands outside of Python
def run_cmd(cmd):
    print("Called")
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
    output = p.communicate()[0]
    return output

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

@app.route("/stop")
def stop_stream():
    run_cmd('mpc stop')
    return redirect('/')

@app.route("/<string:stream_url>")
def mpc_play(stream_url):
    print("called")
    run_cmd('mpc clear')
    run_cmd( ['mpc add %s' % (stream_url)])
    run_cmd('mpc play')
    return redirect('/')

def get_stream():
    usr_id = "andy"
    entries = get_entry(usr_id)

    return entries


if __name__ == "__main__":
    app.run(debug = True)
