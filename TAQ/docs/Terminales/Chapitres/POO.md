# Programmation Orientée Objet (POO)

## Introduction
La **programmation orientée objet (POO)** est une manière d’organiser un programme en regroupant dans des structures appelées **classes** à la fois des données (attributs) et les actions qui peuvent être réalisées sur ces données (méthodes).  

Cette approche permet de représenter des concepts de manière claire et structurée : chaque objet manipulé dans le programme est une instance d’une classe, c’est-à-dire une version concrète du modèle défini.  

La POO facilite la lecture, la réutilisation et l’évolution du code, en rapprochant la logique du programme de la façon dont on décrit et organise les choses dans la vie courante.

👉 Exemple concret :  
- Une **classe** est comme un *modèle* ou un *plan*.  
- Une **instance (objet)** est un *exemplaire concret* de ce modèle.

<span style="color:blue">Exemple</span>

- La **classe** `Stylo` décrit ce qu’est un stylo en général : une couleur d’encre, une longueur, une marque…  
- Les **instances** sont des stylos précis :  
  - `stylo1` : Bic bleu de 15 cm  
  - `stylo2` : Pilot noir de 13 cm  

En Python, on écrira une classe `Stylo`, puis on créera plusieurs objets `stylo1`, `stylo2`, etc.

👉 **À retenir : Une classe est un modèle, une instance est une utilisation concrète de ce modèle.**

---

## Écrire une classe en Python

Exemple : un **rectangle**.

```python
class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur   # attribut
        self.hauteur = hauteur   # attribut

    def aire(self):
        return self.largeur * self.hauteur   # méthode

    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)  # méthode
```

## Créer une instance (objet)

```python
# Création de deux rectangles (instances)
rect1 = Rectangle(5, 2)
rect2 = Rectangle(10, 3)

print(rect1.aire())      # 10
print(rect2.perimetre()) # 26
```

- Rectangle est le plan (classe).
- rect1 et rect2 sont des rectangles concrets (instances).
- Chaque instance a ses propres valeurs d’attributs.

## Accéder aux attributs et méthodes

Attributs :

```python
print(rect1.largeur)   # 5
print(rect2.hauteur)   # 3
```

Méthodes

```python
print(rect1.aire())       # 10
print(rect2.perimetre())  # 26
```

## Exemples supplémentaires

```python
class Livre:
    def __init__(self, titre, auteur, pages):
        self.titre = titre
        self.auteur = auteur
        self.pages = pages

    def resume(self):
        return f"{self.titre}, écrit par {self.auteur} ({self.pages} pages)"

livre1 = Livre("1984", "George Orwell", 328)
print(livre1.resume())  
# affiche : 1984, écrit par George Orwell (328 pages)
```
```python
class Animal:
    def __init__(self, nom, espece, age):
        self.nom = nom
        self.espece = espece
        self.age = age

    def presentation(self):
        return "Je suis " + str(self.nom) + " un " print(self.espece) + " de " + str(self.age) + " ans."

animal1 = Animal("Milo", "chat", 3)
animal2 = Animal("Rex", "chien", 5)

print(animal1.presentation())  # Je suis Milo, un chat de 3 ans.
print(animal2.presentation())  # Je suis Rex, un chien de 5 ans.
```

---
<span style="color:red">Exercices</span>
(Les trois premiers exercices viennent du site [KXS](https://kxs.fr/cours/poo/exercices)

## Exercice 1

1. Créez une classe **Point** qui possède deux attributs `x` et `y` correspondant aux coordonnées du point. Ces deux attributs doivent être affectés par le constructeur.  
2. Ajoutez une méthode `affiche()` qui affiche les coordonnées du point comme ci-dessous (ici, x = 2 et y = 3) :  

    Point | x : 2 | y : 3


3. Ajoutez une méthode `translater(tx, ty)` qui ajoute `tx` à `x` et `ty` à `y`.

## Exercice 2

1. Créez une classe **Compte** modélisant un compte en banque.  
La classe possède deux attributs `somme` et `taux` correspondant à la somme placée sur le compte et au taux d'intérêt. Ces deux attributs doivent être affectés par le constructeur.  
2. Ajoutez une méthode `affiche()` qui affiche la somme et le taux comme ci-dessous :  

    Compte | somme : 2000€ | taux : 2%


3. Ajoutez une méthode `depot(x)` qui ajoute `x` à la somme sur le compte.  
4. Ajoutez une méthode `retrait(x)` qui enlève `x` à la somme sur le compte.  
    Elle pourra renvoyer une erreur si la somme sur le compte devient négative et annuler alors l'opération.  
5. Ajoutez une méthode `interets()` qui calcule les intérêts perçus en un an et les ajoute à la somme placée.  
    Pour rappel, les intérêts se calculent avec la formule :  `interets = taux × somme / 10`

## Exercice 3

1. En vue de faire un site web recensant des citations de films, créez une classe **Citation** permettant d'enregistrer le texte de la citation et son film.  
2. Créez une méthode `affiche()` permettant d'afficher la citation de cette façon :  

    Si je connaissais le con qu’a fait sauter le pont !  
    -- On a retrouvé la 7e compagnie


3. Ajoutez deux attributs `vote_plus` et `vote_moins` pour enregistrer les votes des utilisateurs sur chaque citation.  
4. Ajoutez deux méthodes `vote_pour()` et `vote_contre()` qui permettent respectivement d'incrémenter `vote_plus` et `vote_moins`.  
5. Enfin, ajoutez une méthode `affiche_votes()` qui affiche le nombre de votes pour et le nombre de votes contre la citation.  

## Exercice 4 – Gestion d’une bibliothèque simplifiée

1. Créez une classe **Livre** avec les attributs `titre` et `auteur`.  
   Ajoutez une méthode `affiche()` qui affiche un livre de la forme :  

   "Le Seigneur des Anneaux" de Tolkien

2. Créez une classe **Bibliotheque** qui contient un attribut `livres` initialisé à une liste vide.  
   Ajoutez une méthode `ajoute_livre(livre)` qui permet d’ajouter un objet `Livre` à la liste.  

3. Ajoutez une méthode `affiche()` qui affiche tous les livres de la bibliothèque avec un numéro devant chacun. Exemple :  

    1 - "Le Seigneur des Anneaux" de Tolkien
    2 - "Vingt mille lieues sous les mers" de Jules Verne

4. Ajoutez une méthode `recherche(titre)` qui affiche tous les livres dont le titre contient le mot recherché.  

## Exercice 5 – Jeu de dés

1. Créez une classe **De** avec un attribut `faces` (par défaut 6) et une méthode `lancer()` qui renvoie un nombre aléatoire entre 1 et `faces`.  

2. Créez une classe **Joueur** avec les attributs `nom` et `score` (initialisé à 0).  
Ajoutez une méthode `jouer(de)` qui lance le dé passé en paramètre et ajoute le résultat au score du joueur.  

3. Créez une classe **Partie** avec les attributs `joueurs` (liste d’objets `Joueur`) et `de` (un objet `De`).  
Ajoutez une méthode `tour()` qui fait jouer tous les joueurs une fois.  

4. Ajoutez une méthode `vainqueur()` qui affiche le nom du joueur avec le plus grand score.  
