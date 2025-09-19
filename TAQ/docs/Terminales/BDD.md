# 🌐 Cours Terminale NSI – Bases de données

## 🎯 Objectifs du chapitre
À la fin de ce cours, vous devez être capables de :
- Comprendre le modèle relationnel (tables, attributs, clés).
- Distinguer structure et contenu d’une base de données.
- Manipuler une base de données via SQL (interrogation et mise à jour).
- Connaître le rôle d’un SGBD (sécurité, efficacité, persistance).
- Porter un regard critique sur l’usage des données (confidentialité, RGPD).

---

## 1. Introduction
Une **base de données** est un outil permettant de stocker, organiser et manipuler de grandes quantités de données.  
Exemples :
- Amazon → millions de commandes et utilisateurs.  
- Spotify → catalogues de musiques, playlists personnelles.  
- Un lycée → notes, emplois du temps, enseignants, salles.  

👉 Les simples **tableaux** vus en Première ne suffisent plus : il faut un modèle plus robuste → **le modèle relationnel**.

---

## 2. Le modèle relationnel
### Concepts de base
- **Relation** = table.  
- **Attribut** = colonne.  
- **Tuple** = ligne.  
- **Domaine** = type des valeurs d’une colonne.  

### Les clés
- **Clé primaire** : identifie de manière unique un enregistrement.  
- **Clé étrangère** : fait le lien entre deux tables.  

### Exemple : base Lycée
```
Élèves(id_eleve, nom, prenom, classe)
Professeurs(id_prof, nom, discipline)
Cours(id_cours, matière, id_prof)
Inscription(id_eleve, id_cours, note)
```

📌 **À retenir :**  
Un schéma relationnel décrit la **structure** de la base, pas encore son contenu.  
Il impose des contraintes d’intégrité (unicité, références valides).

---

## 3. SGBD (Système de Gestion de Base de Données)
Un **SGBD** (ex. MySQL, PostgreSQL, SQLite) assure :  
- La **persistance** des données (elles survivent à l’arrêt du programme).  
- La **sécurité** (contrôle des accès).  
- La **gestion des accès concurrents** (plusieurs utilisateurs).  
- L’**optimisation des requêtes** (rapidité).  

⚠️ Enjeux citoyens : Big Data, confidentialité, RGPD.

---

## 4. Le langage SQL – Requêtes d’interrogation
### Structure générale
```sql
SELECT attributs
FROM table
WHERE condition;
```

### Exemples
- Tous les films :
```sql
SELECT * FROM Films;
```
- Films sortis après 2020 :
```sql
SELECT titre, annee
FROM Films
WHERE annee > 2020;
```
- Trier les films par date :
```sql
SELECT titre, annee
FROM Films
ORDER BY annee DESC;
```
- Nombre de spectateurs pour un film :
```sql
SELECT COUNT(*) 
FROM Reservations
WHERE id_film = 3;
```
- Jointure (films + réalisateurs) :
```sql
SELECT Films.titre, Realisateurs.nom
FROM Films
JOIN Realisateurs ON Films.id_realisateur = Realisateurs.id_realisateur;
```

📌 **À retenir :**  
Les clauses principales sont `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `JOIN`.

---

## 5. Le langage SQL – Requêtes de mise à jour
- **Insertion** :
```sql
INSERT INTO Films (id_film, titre, annee)
VALUES (5, "Inception", 2010);
```
- **Mise à jour** :
```sql
UPDATE Films
SET annee = 2012
WHERE id_film = 5;
```
- **Suppression** :
```sql
DELETE FROM Films
WHERE id_film = 5;
```

---

## 6. Exercices pour s’entraîner
### Exercice 1 – Schéma relationnel
Proposez un schéma relationnel pour gérer une bibliothèque (livres, auteurs, emprunteurs, prêts).

### Exercice 2 – Interrogation
Sur la base Cinéma :
1. Lister tous les films.  
2. Trouver les films d’un réalisateur donné.  
3. Donner le nombre de spectateurs pour chaque film.  

### Exercice 3 – Mise à jour
Toujours sur la base Cinéma :
1. Ajouter un nouveau film.  
2. Mettre à jour la date d’une séance.  
3. Supprimer un spectateur.  

---

## 7. Synthèse et ouverture
- Le **modèle relationnel** permet d’organiser les données en tables reliées par des clés.  
- Le **SGBD** garantit sécurité, rapidité et gestion multi-utilisateurs.  
- Le **SQL** est le langage universel pour interroger et modifier les bases.  

🔎 **Ouverture** : les bases NoSQL (MongoDB, Cassandra…) apparaissent pour répondre aux besoins du Big Data.  

---

## 📚 Supports et outils
- Exercices papier (schéma relationnel).  
- TP SQLite (local ou en ligne : [SQLite Online](https://sqliteonline.com/)).  
- Études de cas réalistes : lycée, cinéma, bibliothèque.  
- Ressources RGPD : [CNIL](https://www.cnil.fr/).  
