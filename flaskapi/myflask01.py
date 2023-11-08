from flask import Flask, redirect, url_for

# app represents the web app we are building
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/char")
def get_characters():
    return "You know nothing, Jon Snow"


# with route params
@app.route("/char/<someone>")
def get_specific_character(someone: str):
    return f"You know nothing, {someone}"


# redirection
@app.route("/c/<someone>")
def get_short_character(someone: str):
    # return redirect(f"/char/{someone}")
    # same as above but more flexible when we need to change route in future
    # as it doesn't depend on the harcoded url
    return redirect(url_for("get_specific_character", someone=someone))


@app.route("/books")
def get_books():
    return {"book 1": "Game of Thrones"}


# Start the application
app.run(host="0.0.0.0", port=2224, debug=True)
