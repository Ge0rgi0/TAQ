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
        return f"Je suis {self.nom}, un {self.espece} de {self.age} ans."

animal1 = Animal("Milo", "chat", 3)
animal2 = Animal("Rex", "chien", 5)

print(animal1.presentation())  # Je suis Milo, un chat de 3 ans.
print(animal2.presentation())  # Je suis Rex, un chien de 5 ans.
```

<span style="color:red">Exercice</span>  

On veut représenter des **livres** en Python à l’aide de la programmation orientée objet.

### Étape 1 : Création de la classe
Écrire une classe `Livre` qui possède :  
- trois **attributs** : `titre`, `auteur`, `genre`  
- une **méthode** `resume()` qui renvoie une chaîne de caractères sous la forme :  
  `"Titre (Auteur) - genre"`

### Étape 2 : Création d’instances
Choisissez au moins 3 livres que vous aimez, et pour chacun d'eux creer une instance de la classe 'Livre'.

### Étape 3 : Manipulation des objets
1. Afficher le résumé de chaque livre en utilisant la méthode `resume()`.  
2. Accéder directement à l’attribut `titre` du premier livre et l’afficher.  
3. Modifier l’attribut `genre` du deuxième livre (par exemple, remplacer `"roman"` par `"science-fiction"`) puis afficher à nouveau son résumé pour vérifier le changement.  
4. Ranger les trois livres dans une liste `bibliotheque`, puis parcourir la liste pour afficher le résumé de chaque livre.

### Étape 4 : Personnalisation
Ajoutez une nouvelle méthode `est_du_genre(self, genre_recherche)` qui renvoie **True** si le livre appartient au genre demandé, et **False** sinon.  

Testez-la en vérifiant si vos livres appartiennent au genre `"science-fiction"`.

### Étape 5 : Implication personnelle
1. Dans la liste `bibliotheque`, écrivez une boucle qui affiche uniquement les livres d’un genre que **vous aimez**.  
   (par exemple, tous les `"fantasy"` ou `"roman"`)  
2. Ajoutez un quatrième livre que vous n’aimez pas. Puis affichez tous les livres, mais en marquant ceux que vous n’aimez pas avec la mention `"(rejeté)"`.

### Étape 6 : Créativité
Imaginez une nouvelle méthode pour la classe `Livre`.  
Quelques idées possibles :  
- `changer_titre(self, nouveau_titre)` pour modifier le titre  
- `presentation_longue(self)` qui donne une description plus détaillée  
- `est_du_meme_auteur(self, autre_livre)` qui compare deux livres  

Implémentez la méthode de votre choix, puis testez-la avec vos objets.
