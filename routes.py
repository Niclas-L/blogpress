from flask import redirect, render_template, request, session
from app import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/user/<int:id>")
def user(id):
    return render_template("user.html", id=id)
