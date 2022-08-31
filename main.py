from flask import Flask, request, render_template
app = Flask(__name__)

from ordinaland import *


@app.route("/")
def index():
    return render_template("index.html")

"""
@app.route("/blog/{num_page}")

@app.route("/article/{num_article}")

@app.route("/glossaire")

@app.route("/glossaire/{mot}")

@app.route("/contact")

@app.route("/monter-ordinateur")

@app.route("/afficher-ordinateur", methods=['POST'])
"""


if __name__ == "__main__":
    app.run(debut = True)