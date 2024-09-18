from flask import render_template
from app import app


# @app.route("/blog")
# def blog():
#     return "Blog menu"


@app.route("/")
def index():
    animal = "Tiger"
    return render_template("index.html", name=animal)
