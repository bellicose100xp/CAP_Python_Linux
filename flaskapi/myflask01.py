from flask import Flask

# app represents the web app we are building
app = Flask(__name__)

# the following code teaches our app "how to app"


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/characters")
def get_characters():
    return "You know nothing, Jon Snow"


@app.route("/books")
def get_books():
    return {"book 1": "Game of Thrones"}


# Start the application
app.run(host="0.0.0.0", port=2224, debug=True)
