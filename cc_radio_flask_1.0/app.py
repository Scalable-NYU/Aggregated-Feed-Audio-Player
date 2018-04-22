from flask import Flask, Response, render_template, redirect, url_for
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
import get_my_tweets as tweets

app = Flask(__name__)
app.secret_key = "supersecret"
blueprint = make_twitter_blueprint(
    api_key = "GNTPJ8alh2T4wC6396QB1qLao",
    api_secret = "5mGnp5fHYea9nf57aiPhOR04wD1oUOJSAsP9rcYQCD2KilvPJn"
)
app.register_blueprint(blueprint, url_prefix="/login")

# def streamwav():
#     def generate():
#         with open("cc_audio_example/test.mp3", "rb") as fwav:
#             data = fwav.read(1024)
#             while data:
#                 yield data
#                 data = fwav.read(1024)
#     return Response(generate(), mimetype="audio/x-wav")

@app.route("/")
def index():
    if not twitter.authorized:
        return redirect(url_for("twitter.login"))
    resp = twitter.get("account/settings.json")
    assert resp.ok

    my_tweets = tweets.main()

    return render_template('index.html', display = my_tweets)

    # return "You are @{screen_name} on GitHub".format(screen_name = resp.json()["screen_name"])

# @app.route("/login")
# def 

if __name__ == "__main__":
    app.run(debug = True)