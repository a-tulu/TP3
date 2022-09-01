from flask import Flask, request, render_template
app = Flask(__name__)

from ordinaland import *


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/article")
def article():
    return render_template('article.html')

@app.route("/glossaire")
def glossaire():
    return render_template('glossaire.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/monter-ordinateur")
def construire():
    return render_template('construire.html')


if __name__ == "__main__":
    app.run(debug = True)

