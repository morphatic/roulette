from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, Reilly!</p>"


@app.route("/greet", methods=["POST"])
@app.route("/greet/<name>", methods=["GET"])
def greeting(name=None):
    name = name if name is not None else request.form["name"]
    return render_template("index.html", greeting=greet(name))


@app.route("/form")
def name_form():
    return render_template("form.html")


def greet(name):
    return f"Hello, {name}!"
