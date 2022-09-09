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
    order_info = {}
    cost = []

    order_info['case'] = request.form.get('case')
    for cases in choix_composantes['case']:
        if cases.description == order_info['case']:
            cost.append(cases.prix)

    order_info['motherboard'] = request.form.get('motherboard')
    for motherboards in choix_composantes['motherboard']:
        if motherboards.description == order_info['motherboard']:
            cost.append(motherboards.prix)

    order_info['cpu'] = request.form.get('cpu')
    for cpus in choix_composantes['cpu']:
        if cpus.description == order_info['cpu']:
            cost.append(cpus.prix)

    order_info['storage'] = request.form.get('storage')
    for storages in choix_composantes['storage']:
        if storages.description == order_info['storage']:
            cost.append(storages.prix)

    order_info['cooling'] = request.form.get('cooling')
    for coolings in choix_composantes['cooling']:
        if coolings.description == order_info['cooling']:
            cost.append(coolings.prix)

    order_info['ram'] = request.form.get('ram')
    for rams in choix_composantes['ram']:
        if rams.description == order_info['ram']:
            cost.append(rams.prix)

    order_info['power'] = request.form.get('power')
    for powers in choix_composantes['power']:
        if powers.description == order_info['power']:
            cost.append(powers.prix)

    order_info['keyboard'] = request.form.get('keyboard')
    for keyboards in choix_composantes['keyboard']:
        if keyboards.description == order_info['keyboard']:
            cost.append(keyboards.prix)

    order_info['mouse'] = request.form.get('mouse')
    for mouses in choix_composantes['mouse']:
        if mouses.description == order_info['mouse']:
            cost.append(mouses.prix)

    order_info['monitor'] = request.form.get('monitor')
    for monitors in choix_composantes['monitor']:
        if monitors.description == order_info['monitor']:
            cost.append(monitors.prix)

    order_info['postalcode'] = request.form.get('postalcode')
    postal_code = request.form.get('postalcode')

    ordi = Ordinateur()
    ordi.composantes = cost

    return render_template('afficher-ordinateur.html', order = order_info, choix = choix_composantes,
                           subtotal = ordi.sous_total(), tax = ordi.taxes(ordi.sous_total()),
                           grand_total = ordi.total(ordi.sous_total(), ordi.taxes(ordi.sous_total()), Ordinateur.livraison(postal_code)),
                           postalcode = Ordinateur.livraison(postal_code))


if __name__ == "__main__":
    app.run(debug = True)

