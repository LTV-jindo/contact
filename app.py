from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK")


@app.route("/")
def home():
    if DISCORD_WEBHOOK:
        try:
            requests.post(
                DISCORD_WEBHOOK,
                json={"content": "🔔 Someone need contact!"},
                timeout=5
            )
        except requests.RequestException:
            pass

    return render_template("index.html")


if __name__ == "__main__":
    app.run()