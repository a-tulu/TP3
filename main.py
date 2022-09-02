from flask import Flask, request, render_template
app = Flask(__name__)

from ordinaland import *


@app.route("/")
def index():
    articles_selectionners = [0, 5, 12]
    articles_variables = []

    for nb_article in articles_selectionners:

        article = articles[nb_article].texte
        article_split = article.split("\n\n")

        tableau_article = []
        for paragraphe in range(len(article_split)):
            if article_split[paragraphe] != "":
                tableau_article.append(article_split[paragraphe])

        tableau_article_sans_n = []
        for texte in range(len(tableau_article)):
            texte_sans_n = tableau_article[texte].replace("\n", " ")
            tableau_article_sans_n.append(texte_sans_n)

        articles_variables.append(articles[nb_article].titre)

        if len(tableau_article_sans_n) >= 2:
            string_deux_paragraphes = tableau_article_sans_n[0] + "\n\n" + tableau_article_sans_n[1]
            articles_variables.append(string_deux_paragraphes)
        else:
            articles_variables.append(tableau_article_sans_n[0])

    print(articles_variables[1])

    return render_template('index.html', var0 = articles_variables[0], var1 = articles_variables[1],
                           var2 = articles_variables[2], var3 = articles_variables[3], var4 = articles_variables[4],
                           var5 = articles_variables[5])

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

