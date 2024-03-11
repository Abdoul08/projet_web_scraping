
/* 
se déplacer dans la base mysql
cd /usr/local/mysql/bin
./mysql -uroot -p

*/
/* creation de la base de donnee*/
create databases web_scraping

/*afficher la liste des bases de données */
show databases;

/*selection une base de données */
use web_scraping;


/* Afficher la liste des tables */
show tables;


/* creation  de la table categorie*/
CREATE TABLE categorie (
    id INT AUTO_INCREMENT PRIMARY KEY,
    libelle VARCHAR(50) NOT NULL
);

/* creation  de la table authentification*/
CREATE TABLE authentification (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prenom VARCHAR(50) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL
    password VARCHAR(255) NOT NULL,
    categorie_id int,
    FOREIGN KEY(categorie_id) REFERENCES categorie(id))
    ;
    /*creation de la table contente*/
    CREATE TABLE contente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Categorie VARCHAR(50) NOT NULL,
    Contenu longtext);
    