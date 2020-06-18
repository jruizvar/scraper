from flask import (
    Flask, redirect, request, send_from_directory, url_for
)
from raspatela import main


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        youtuber = request.form["youtuber"]
        filename = main(youtuber)
        return redirect(url_for("download", filename=filename))
    return """
        <form method='post'>
            <p><input type=text name=youtuber></p>
            <p><input type=submit value=Download></p>
        </form>
    """


@app.route("/<filename>")
def download(filename):
    return send_from_directory("static", filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
