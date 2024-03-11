from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_restful import Api, Resource


import os
import mysql.connector


backend = Flask(__name__)
api = Api(backend)
# backend.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
backend.config['UPLOAD_FOLDER'] = '/data_sources/'

# Configuration de la base de données MySQL
backend.config['MYSQL_HOST'] = 'host.docker.internal'
backend.config['MYSQL_USER'] = 'root' # Utilisateur MySQL
backend.config['MYSQL_PASSWORD'] = '12345678' # Mot de passe MySQL
backend.config['MYSQL_DB'] = 'test' # Base de données MySQL

mysql = mysql.connector.connect(
    host=backend.config['MYSQL_HOST'],
    user=backend.config['MYSQL_USER'],
    password=backend.config['MYSQL_PASSWORD'],
    database=backend.config['MYSQL_DB']
)

@backend.get('/ajout')
def ajout():
        return render_template(('form.html'))

# Classe pour la ressource /insertion
class Insertion_post(Resource):
    def post(self):
        # Insérer le code pour l'insertion ici
        return {"message": "Données insérées avec succès"}, 201

# Classe pour la ressource /update/<int:id>
class Update_post(Resource):
    def put(self, id):
        # Insérer le code pour la mise à jour ici
        return {"message": f"Données avec l'ID {id} mises à jour avec succès"}, 200

# Classe pour la ressource /delete/<int:id>
class Delete_post(Resource):
    def delete(self, id):
        # Insérer le code pour la suppression ici
        return {"message": f"Données avec l'ID {id} supprimées avec succès"}, 200

# ... Définissez d'autres classes de ressources pour chaque point de terminaison ...

# Définir les routes pour chaque classe de ressource
api.add_resource(Insertion_post, '/insertion')
api.add_resource(Update_post, '/update/<int:id>')
api.add_resource(Delete_post, '/delete/<int:id>')





@backend.post('/insertion')
def insertion():
    if request.method == 'POST':
        # if 'fichier' not in request.files:
        #     return 'No file part'
        # fichier = request.files['fichier']
        # if fichier.filename == '':
        #     return 'No selected file'
        # if fichier:
            site = request.form['site']
            # file_data = fichier.read()
            # fichier = request.files['fichier']
            # filename = secure_filename(fichier.filename)

            cur = mysql.cursor()
            cur.execute("INSERT INTO test (site) values(%s)", (site,) )
            #mysql.commit
            mysql.commit()
            cur.close()
            return redirect(url_for('index'))





#affichage des resultats
# @backend.get('/')
# def indexe():
#     cur = mysql.cursor()   
#     cur.execute("select * from test")
#     # cur.connection.commit()
#     sites = cur.fetchall()
#     # print(sites)
#     cur.close()
#     return render_template("index.html", data=sites)
    #envoi des informations a la page d'accueil
    # return jsonify(sites)

# Route pour obtenir une tâche par son ID (GET)

@backend.route("/update/<int:id>",methods=['PUT','POST',"GET"])

def update(id):
    if request.method in ["POST","PUT"]:
        site = request.form['site']
        # dump(site)
        cur = mysql.cursor()
        cur.execute("UPDATE test SET site=%s WHERE id=%s", (site, id))
        mysql.commit()
        # print(cur)
        cur.close()
        return redirect(url_for('index'))
        # return render_template("index.html")


@backend.route('/liens_update/<int:id>',methods=["GET"])
def liens_update(id):
    cur = mysql.cursor()
    cur.execute("SELECT * FROM test WHERE id = %s", (id,))
    update = cur.fetchone()
    cur.close()
    if update:
        return render_template('update.html', update=update)
    else:
        return jsonify({'message': 'Tâche non trouvée'}), 404

@backend.route('/delete/<int:id>', methods=["DELETE","GET","POST"])
def delete(id):
    # if request.form.get('_method') in ['DELETE',"GET","POST"]:
        cur = mysql.cursor()
        cur.execute("DELETE FROM test WHERE id=%s", (id,))
        mysql.commit()
        cur.close()
        return render_template("index.html")
    # return jsonify({'message': f"""La suppression de l'id ${id} a été effectuée avec succès"""}), 200





#categorie
@backend.route("/categorie_form",methods=["GET"])
def categorie_form():
    return render_template("categorie_form.html")

#tableau des donnees dans la base 
@backend.route("/categorie_index",methods=["GET"])
def categorie_index():
    cur = mysql.cursor()
    cur.execute("SELECT * FROM categorie")
    result = cur.fetchall()
    cur.close()

    return render_template("categorie_index.html",result = result)

@backend.route("/categorie_update",methods=['PUT','POST',"GET"])

def categorie_update():
    if request.method in ["POST","PUT"]:
        libelle = request.form['libelle']
        id = request.form['categorie_id']
        # dump(site)
        cur = mysql.cursor()
        cur.execute("UPDATE categorie SET libelle=%s WHERE id=%s", (libelle, id))
        mysql.commit()
        # print(cur)
        cur.close()
        return redirect(url_for('categorie_index'))
        # return render_template("categorie_index.html")


@backend.route('/categorie_liens_update/<int:id>',methods=["GET"])
def categorie_liens_update(id):
    cur = mysql.cursor()
    cur.execute("SELECT * FROM categorie WHERE id = %s", (id,))
    update = cur.fetchone()
    cur.close()
    if update:
        return render_template('categorie_update.html', update=update)
    else:
        return jsonify({'message': 'Tâche non trouvée'}), 404

#delete categorie
@backend.route('/categorie_delete/<int:id>', methods=["DELETE","GET","POST"])
def categorie_delete(id):
    # if request.form.get('_method') in ['DELETE',"GET","POST"]:
        cur = mysql.cursor()
        cur.execute("DELETE FROM categorie WHERE id=%s", (id,))
        mysql.commit()
        cur.close()
        return redirect(url_for('categorie_index'))
        
        # return render_template("categorie_index.html")






#insertion dans la base categorie
@backend.route('/insertion_categorie', methods=["POST"])
def insertion_categorie():
    if request.method == "POST":
        libelle = request.form['libelle']
        cur = mysql.cursor()
        cur.execute("INSERT INTO categorie (libelle) values(%s)", (libelle,) )
        #mysql.commit
        mysql.commit()
        cur.close()
        return redirect(url_for('categorie_index'))



#utilisateur
@backend.route('/register',methods=["GET"])
def register():
    cur = mysql.cursor()
    cur.execute("SELECT * FROM categorie")
    categorie = cur.fetchall()
    cur.close()
    return render_template("register.html",categories = categorie)

@backend.route("/insertion_user", methods=["POST"])
def insertion_user():
    if request.method == "POST":
        prenom = request.form['prenom']
        nom = request.form['nom']
        email = request.form['email']
        password = request.form['password']
        categorie_id = request.form['categorie_id']
        cur = mysql.cursor()
        cur.execute("INSERT INTO user (prenom,nom,email,password,categorie_id) values(%s,%s,%s,%s,%s)", (prenom,nom,email,password,categorie_id) )
        #mysql.commit
        mysql.commit()
        cur.close()
        return render_template('login.html')


#connexion 

@backend.route('/connexion_user', methods=["POST","GET"])
def connexion_user():
    if request.method == 'POST':
        email = request.form['email']
        passw = request.form['password']

        cur = mysql.cursor()
        cur.execute("SELECT * FROM user WHERE email =%s and  password= %s", (email,passw))
        result = cur.fetchall()
        
        cur.close()
        if result :
            return  redirect(url_for("index"))
        else:
            error = 'Mauvaises informations d\'authentification. Veuillez réessayer.'
            return render_template('login.html', error=error)

#accueil utilisateur
@backend.route("/index_user", methods=["GET"])
def index_user():
    cur = mysql.cursor()
    cur.execute("SELECT * FROM user, categorie where user.categorie_id=categorie.id")
    result = cur.fetchall()
    print(result)
    cur.close()
    return render_template("index_user.html",result = result)

#mise a jour de l'utilisateur

@backend.route("/user_update",methods=['PUT','POST',"GET"])

def user_update():
    if request.method in ["POST","PUT"]:
        user_id = request.form['user_id']
        prenom = request.form['prenom']
        nom = request.form['nom']
        email = request.form['email']
        categorie_id = request.form['categorie_id']
        # dump(site)
        cur = mysql.cursor()
        cur.execute("UPDATE user SET prenom=%s,nom=%s,email=%s,categorie_id=%s WHERE id=%s", (prenom,nom,email,categorie_id,user_id))
        mysql.commit()
        # print(cur)
        cur.close()
        return redirect(url_for('index_user'))

        # return render_template("index_user.html")


@backend.route('/user_liens_update/<int:id>',methods=["GET"])
def user_liens_update(id):
    cur = mysql.cursor()
    cur.execute("SELECT * FROM user,categorie WHERE user.categorie_id=categorie.id and user.id = %s", (id,))
    update = cur.fetchone()
    cat = mysql.cursor()
    cat.execute("SELECT * FROM categorie")
    categories = cat.fetchall()
    cat.close()
    cur.close()
    # print(update)
    if update:
        return render_template('user_update.html', update=update,categories=categories)
    else:
        return jsonify({'message': 'Tâche non trouvée'}), 404

# result = user_liens_update(id)
# print(result)


#delete categorie
@backend.route('/user_delete/<int:id>', methods=["DELETE","GET","POST"])
def user_delete(id):
    # if request.form.get('_method') in ['DELETE',"GET","POST"]:
        cur = mysql.cursor()
        cur.execute("DELETE FROM user WHERE id=%s", (id,))
        mysql.commit()
        cur.close()
        return redirect(url_for('index_user'))
        # return render_template("index_user.html")

@backend.get('/')
def index():
    cur = mysql.cursor()
    cur.execute("SELECT  SUM(CASE WHEN Categorie = 'fourniture_bureau' THEN 1 ELSE 0 END) AS nb_fourniture_bureau, SUM(CASE WHEN Categorie = 'btp' THEN 1 ELSE 0 END) AS nb_btp, SUM(CASE WHEN Categorie = 'autres' THEN 1 ELSE 0 END) AS nb_autres FROM test;")
    index = cur.fetchone()

    cat = mysql.cursor()
    cat.execute("SELECT count(*) FROM user")
    update = cat.fetchone()
    # nombre_categorie_int = [int(x) for x in index]
    cur.close()
    cat.close()
    return render_template("index.html" ,nombre_categorie = index ,update=update)
    # render_template("login.html")

@backend.route("/index_front",methods=['GET'])
def index_front():
    cur = mysql.cursor()
    cur.execute("SELECT Categorie, SUM(CASE WHEN Categorie = 'fourniture_bureau' THEN 1 ELSE 0 END) AS nb_fourniture_bureau, SUM(CASE WHEN Categorie = 'btp' THEN 1 ELSE 0 END) AS nb_btp, SUM(CASE WHEN Categorie = 'autres' THEN 1 ELSE 0 END) AS nb_autres FROM test GROUP BY Categorie;")
    rows = cur.fetchall()

    # Créer un dictionnaire pour stocker les résultats
    categories = {}
    for row in rows:
        categories[row[0]] = {'nb_fourniture_bureau': row[1], 'nb_btp': row[2], 'nb_autres': row[3]}
    cur.close()
    return jsonify(categories)
    # return jsonify(index)


@backend.route("/login",methods=['GET'])
def login():
    return render_template("login.html")

if __name__ == '__main__':
    backend.run(debug=True)