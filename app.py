from flask import Flask, send_from_directory
from raspatela import main


app = Flask(__name__)


@app.route("/")
def index():
    return "Use the URL /&#60 youtuber &#62 to get the data"


@app.route("/<youtuber>")
def getdata(youtuber):
    filename = main(youtuber)
    return f"File available at the URL /{filename}"


@app.route("/<filename>")
def download(filename):
    return send_from_directory("static", filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
