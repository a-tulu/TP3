from flask import Flask, request, render_template
app = Flask(__name__)

from ordinaland import *


@app.route("/")
def index():

    articles_variables = Article.lire_deux_paragraphes()

    return render_template('index.html', var0 = articles_variables[0], var1 = articles_variables[1],
                           var2 = articles_variables[2], var3 = articles_variables[3], var4 = articles_variables[4],
                           var5 = articles_variables[5])

@app.route("/blog/<id>")
def blog(id):
    nb_articles = len(articles)
    nb_pages = nb_articles // 3
    if nb_pages != 0:
        nb_pages += 1
    id_int = int(id)

    if not id_int <= nb_pages:
        return render_template('index.html')
    else:

        return render_template('blog.html', var0 = nb_pages, var1 = id_int, var2 = Article.lire_deux_paragraphes(),
                               var3 = len(Article.lire_deux_paragraphes()))

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

