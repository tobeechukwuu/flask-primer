from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome Tobe!"


@app.route("/hello/<string:name_to_greet>/")  # the converter is string and variable name is name_to_greet
def hello(name_to_greet):
    return "Hello %s, greetings from Flask Framework!" % name_to_greet


@app.route("/about-us/")
def about_us():
    return "We are here to serve you!"


if __name__ == "__main__":
    app.run()
