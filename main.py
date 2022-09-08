from flask import Flask, request, render_template
app = Flask(__name__)

from ordinaland import *


@app.route("/")
def index():
    articles_variables = Article.lire_deux_paragraphes()
    return render_template('index.html', var0 = articles_variables[0], var1 = articles_variables[1], id_1 = 0,
                           var2 = articles_variables[2], var3 = articles_variables[3], id_2 = 1,
                           var4 = articles_variables[4], var5 = articles_variables[5], id_3 = 2)

@app.route("/blog/<id>")
def blog(id):
    nb_articles = len(articles)
    nb_pages = nb_articles // 3
    if nb_pages != 0:
        nb_pages += 1
    id_int = int(id)
    tableau_titre = []
    for art in articles:
        tableau_titre.append(art.titre)

    return render_template('blog.html', var0 = nb_pages, var1 = id_int, var2 = Article.lire_deux_paragraphes(),
                               var3 = len(Article.lire_deux_paragraphes()), tab_titres = tableau_titre)

@app.route("/article/<id>")
def article(id):
    id_int = int(id)
    return render_template('article.html', titres = articles[id_int].titre, date = articles[id_int].date,
                           temps = Article.temps_lecture(articles[id_int]), image = articles[id_int].image,
                           texte = articles[id_int].texte, id = id_int, articles = len(articles), tableau = articles)

@app.route("/glossaire")
def glossaires():
    return render_template('glossaire.html', glos = glossaire)

@app.route("/glossaire/<id>")
def definition(id):
    for objet in glossaire:
        if id == objet.terme:
            place = glossaire.index(objet)
    return render_template('definition.html', mot = id, glos = glossaire, place = place,
                           relie = Definition.termes_relies(glossaire[place]))

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/construire")
def construire():
    return render_template('construire.html', choix = choix_composantes)

@app.route("/afficher-ordinateur", methods = ['POST'])
def afficher():
    codepostal = request.form['postalcode']
    monitor = request.form['monitor']
    return render_template('afficher-ordinateur.html', postalcode = codepostal)


if __name__ == "__main__":
    app.run(debug = True)

