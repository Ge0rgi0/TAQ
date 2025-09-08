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