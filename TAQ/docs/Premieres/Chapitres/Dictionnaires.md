# Les Dictionnaires

## Qu'est-ce qu'un dictionnaire ?

Un **dictionnaire** est une structure de données permettant d'associer des **clés** à des **valeurs**.  
Contrairement aux listes, où on accède aux éléments par un indice, ici on accède par une clé.

Exemple :

``` python
notes = {"Alice": 15, "Bob": 12, "Claire": 18}

print(notes["Bob"])    # affiche 12
print(notes["Claire"]) # affiche 18
```

Les accolades `{}` permettent de définir un dictionnaire.  
*Les clés doivent être uniques et immuables* (entiers, flottants, chaînes, booléens, tuples, par exemples).

------------------------------------------------------------------------

## Créer et modifier un dictionnaire

### Création

``` python
personne = {"nom": "Dupont", "age": 30}
```

### Ajouter une clé

``` python
personne["ville"] = "Paris"
```

### Modifier une valeur

``` python
personne["age"] = 31
```

### Supprimer une clé

``` python
del personne["ville"]
```

### Vérifier la présence d'une clé

``` python
print("nom" in personne)  # True
print("adresse" in personne)  # False
```

### Longueur

``` python
print(len(personne))  # nombre de paires clé/valeur
```

------------------------------------------------------------------------

## Parcourir un dictionnaire

### Parcourir les clés

``` python
for cle in personne:
    print(cle)
```

ou bien

``` python
for cle in personne.keys():
    print(cle)
```

*la methode `keys()` renvoit la liste des clés du dictionnaires*
*`personne.keys()` renvoit `["nom", "age"]`*

### Parcourir les valeurs

``` python
for valeur in personne.values():
    print(valeur)
```

*la methode `values()` renvoit la liste des valeurs du dictionnaires*
*`personne.values()` renvoit `["Dupont", 30]`*

### Parcourir clés + valeurs

``` python
for cle, valeur in personne.items():
    print(cle, ":", valeur)
```

*la methode `items()` renvoit la liste couples (clé, valeur) du dictionnaires*
*`personne.items()` renvoit `[("nom", "Dupont"), ("age", 30)]`*

------------------------------------------------------------------------

## Exemple d'utilisation

``` python
notes = {"Alice": 10, "Bob": 15, "Claire": 12}

somme = 0
for n in notes.values():
    somme += n

m = somme / len(notes)
print(m)
```

*Que fait ce programme ?*

------------------------------------------------------------------------

# Exercices

## 1. Accès et ajout

Créer un dictionnaire `eleve = {"nom": "Lena", "classe": "1ère"}`  
Ajouter une clé `"age"` avec la valeur 16.

------------------------------------------------------------------------

## 2. Mise à jour

Créer un dictionnaire représentant un produit :  
`produit = {"nom": "Stylo", "prix": 2.5}`  
Augmenter le prix de 10%.

------------------------------------------------------------------------

## 3. Comptage

Créer un dictionnaire `scores` avec plusieurs joueurs.  
Écrire un programme qui affiche le nombre total de points.

------------------------------------------------------------------------

## 4. Recherche d'une clé (sans `in`)

Demander un nom à l'utilisateur.  
Vérifier manuellement s'il existe dans le dictionnaire des notes.

------------------------------------------------------------------------

## 5. Trouver la valeur max/min

Sans `max()` ni `min()`, trouver la plus grande et la plus petite valeur
d'un dictionnaire numérique.

------------------------------------------------------------------------

## 6. Inversion clé/valeur

Créer un dictionnaire puis construire un **nouveau dictionnaire** où les
clés deviennent les valeurs et inversement.  
( ! Les valeurs doivent être uniques. ! )

------------------------------------------------------------------------

## 7. Fusion manuelle

Fusionner deux dictionnaires **sans utiliser l'opérateur `|`**.

------------------------------------------------------------------------

## 8. Filtrer un dictionnaire

Créer un dictionnaire de températures par ville.  
Écrire un programme qui construit un nouveau dictionnaire ne contenant que les villes dont la température est \> 20 à partir du premier dictionnaire.

------------------------------------------------------------------------

## 9. Comptage de valeurs

Compter combien de valeurs d'un dictionnaire sont paires / impaires.

------------------------------------------------------------------------

## 10. Final

Créer un dictionnaire vide.  

Tant que l'utilisateur entre une clé :  

- si la clé existe déjà, supprimer sa valeur  
- sinon ajouter une valeur demandée  

Entrer `stop` → afficher le dictionnaire et arrêter.

------------------------------------------------------------------------

# Dictionnaires imbriqués

Un dictionnaire peut contenir d'autres dictionnaires.

``` python
classe = {
    "eleve1": {"nom": "Alice", "age": 15},
    "eleve2": {"nom": "Bob", "age": 16}
}
```

Accès :

``` python
print(classe["eleve1"]["nom"])  # Alice
```

------------------------------------------------------------------------

## Exercices dictionnaires imbriqués

### 1. Affichage formaté

Créer un dictionnaire de personnes et afficher leurs informations ligne
par ligne.

### 2. Somme sur dictionnaire 2D

Calculer la somme de tous les âges.

### 3. Recherche

Demander un nom et vérifier s'il est dans l'un des sous-dictionnaires.

### 4. Max/min

Trouver la personne la plus âgée.

### 5. Transformation

Créer un nouveau dictionnaire ne contenant que les noms.
