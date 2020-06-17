from flask import Flask, send_from_directory
from glob import glob
from raspatela import main


app = Flask(__name__)


@app.route("/")
def index():
    return "Use the URL /<youtuber> to get the data"


@app.route("/<youtuber>")
def download(youtuber):
    main(youtuber)
    filename = glob("static/*.csv")[0][7:]
    return send_from_directory("static", filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
