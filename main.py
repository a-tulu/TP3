from flask import Flask, request, render_template
app = Flask(__name__)

from ordinaland import *


@app.route("/")
def index():

    tableau_deux_paragraphes = Article.lire_deux_paragraphes()

    # Les variables 'id_x' servent à identifier les articles selectionners à en faire un aperçu à partir de leur
    # numéro d'indice.
    return render_template('index.html', id_1 = 0, titre_1 = tableau_deux_paragraphes[0],
                           pg_1 = tableau_deux_paragraphes[1], id_2 = 1, titre_2 = tableau_deux_paragraphes[2],
                           pg_2 = tableau_deux_paragraphes[3], id_3 = 2, titre_3 = tableau_deux_paragraphes[4],
                           pg_3 = tableau_deux_paragraphes[5])

@app.route("/blog/<id>")
def blog(id):

    nb_articles = len(articles)

    # On afficher seulement trois articles par page.
    nb_pages = nb_articles // 3

    # Si le nombre d'articles n'est pas entièrement divisble par trois, on ajoute une page au compte total de pages.
    if (nb_articles % 3) != 0:
        nb_pages += 1

    id_int = int(id)

    # Création d'un tableau de titres pour tous les articles dans le tableau 'articles' pour faciliter son affichage
    # sur la page blog.html.
    tableau_titre = []
    for item in articles:
        tableau_titre.append(item.titre)

    if id_int <= nb_pages:
        return render_template('blog.html', nb_total_pages = nb_pages, page = id_int,
                               tab_deux_pg = Article.lire_deux_paragraphes(),
                               long_tab_deux_pg = len(Article.lire_deux_paragraphes()), tab_titres = tableau_titre)

@app.route("/article/<id>")
def article(id):

    id_int = int(id)

    return render_template('article.html', titre = articles[id_int].titre, date = articles[id_int].date,
                           temps_de_lecture = Article.temps_lecture(articles[id_int]), image = articles[id_int].image,
                           texte = Article.tableau_paragraphes(articles[id_int]),
                           id = id_int, long_tab_articles = len(articles), tab_articles = articles)

@app.route("/glossaire")
def glossaires():
    return render_template('glossaire.html', glossaire = glossaire)

@app.route("/glossaire/<id>")
def definition(id):

    # Vérification que le mot ('id') entré en paramètre est dans le glossaire.
    for item in glossaire:
        if id == item.terme:
            # Si le mot est trouvé dans le glossaire, on garde son index dans le tableau à l'intérieur de la variable
            # 'place' pour pouvoir le retrouver plus facilement dans le glossaire une fois dans la page definition.html.
            place = glossaire.index(item)

    return render_template('definition.html', mot = id, glossaire = glossaire, place = place,
                           termes_relies = Definition.termes_relies(glossaire[place]))

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/construire")
def construire():
    return render_template('construire.html', choix = choix_composantes)

@app.route("/afficher-ordinateur", methods = ['POST'])
def afficher():

    # Ce dictionnaire va contenir tous les informations remplis dans le formulaire de la page construire.html. Les clés
    # vont être le nom des composantes.
    order_info = {}
    # Ce tableau va contenir le prix des composantes selectionnés.
    cost = []
    composants = ['case', 'motherboard', 'cpu', 'storage', 'cooling', 'ram', 'power', 'keyboard', 'mouse', 'monitor']

    for composant in composants:
        order_info[composant] = request.form.get(composant)

        for objet in choix_composantes[composant]:
            # Si un type de composant est selectionner dans la commande, son coût est appendé dans le tableau cost.
            if objet.description == order_info[composant]:
                cost.append(objet.prix)

    order_info['postalcode'] = request.form.get('postalcode')
    postal_code = request.form.get('postalcode')

    # Initialisation d'un objet de la classe Ordinateur. À la place d'ajouter le nom des composantes dans le tableau,
    # j'ai opté pour y mettre les prix des composantes (contenu dans le tableau 'cost').
    ordi = Ordinateur()
    ordi.composantes = cost

    return render_template('afficher-ordinateur.html', order = order_info, choix = choix_composantes,
                           subtotal = ordi.sous_total(), tax = ordi.taxes(ordi.sous_total()),
                           grand_total = ordi.total(ordi.sous_total(), ordi.taxes(ordi.sous_total()), Ordinateur.livraison(postal_code)),
                           postalcode = Ordinateur.livraison(postal_code))


if __name__ == "__main__":
    app.run(debug = True)

