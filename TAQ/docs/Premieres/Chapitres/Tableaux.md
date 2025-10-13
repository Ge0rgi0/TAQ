# Les Tableaux

## Qu’est-ce qu’un tableau ?

Un tableau (ou **liste** en Python) est une structure de données qui permet de stocker plusieurs valeurs dans une seule variable.  
On peut y accéder grâce à des **indices** commençant à 0.

```python
notes = [12, 15, 9, 18]
print(notes[0])  # affiche 12
print(notes[3])  # affiche 18
```

Les crochets `[]` servent à définir une liste.  
Chaque élément peut être de n’importe quel type (entier, flottant, chaîne, booléen, etc.).

---

## Créer et modifier un tableau

### Création
```python
fruits = ["pomme", "banane", "cerise"]
```

### Ajout d’un élément
```python
fruits.append("orange")
```

### Suppression d’un élément
```python
fruits.remove("banane")
```

### Modification d’un élément
```python
fruits[0] = "kiwi"
```

### Taille du tableau
```python
print(len(fruits))  # nombre d'éléments
```

### Concaténation
```Python
a = [1,2]
b = [3,7]
c = a + b #[1,2,3,7]
```

---

## Parcourir un tableau

### Avec une boucle `for`
```python
for fruit in fruits:
    print(fruit)
```

### Avec les indices
```python
for i in range(len(fruits)):
    print("Indice", i, ":", fruits[i])
```

### Exemple d'utilisation

```python
notes = [10, 15, 12, 8, 17]
somme = 0
for note in notes:
    somme += note

m = somme / len(notes)
print(m)
```

---

## Listes et types mélangés

Python autorise les listes contenant plusieurs types de données, même si cela est rarement conseillé pour des programmes bien structurés.

```python
melange = [12, "bonjour", 3.14, True]
```

Il est préférable d’utiliser des tableaux homogènes (tous les éléments du même type).

---

## Exercices

### Somme manuelle
Crée une liste `nombres = [4, 7, 2, 9, 5]`.  
Écris un programme qui calcule **la somme des éléments** sans utiliser la fonction `sum()`.  
Utilise une boucle pour accumuler les valeurs dans une variable.

---

### Recherche du plus grand élément
Crée une liste `notes = [10, 13, 7, 15, 9, 18]`.  
Écris un programme qui trouve **la plus grande note** sans utiliser `max()`.  
Le programme doit comparer les éléments un à un et conserver le plus grand dans une variable.

---

### Recherche du plus petit élément
Crée une liste `notes = [10, 13, 7, 15, 9, 18]`.  
Écris un programme qui trouve **la plus petite note** sans utiliser `min()`.

---

### Compter les valeurs supérieures à un seuil
Crée une liste `temperatures` et un entier `seuil`.  
Écris un programme qui compte **combien de valeurs** dans la liste sont **strictement supérieures** à ce seuil.  
Exemple :  
Pour `temperatures = [18, 22, 19, 25, 17, 21]` et `seuil = 20`, le programme doit afficher `3`.

---

### Recherche d’un élément
Crée une liste de chaînes `mots`.  
Demande à l’utilisateur de saisir un mot.  
Sans utiliser `in`, vérifie **toi-même** si le mot se trouve dans la liste.  
Affiche un message indiquant s’il est présent ou non.

---

### Inversion manuelle d’un tableau
Crée une liste `valeurs = [1, 2, 3, 4, 5]`.  
Écris un programme qui construit **une nouvelle liste contenant les mêmes éléments dans l’ordre inverse**, sans utiliser `reverse()` ni la syntaxe `[::-1]`.  
Utilise une boucle.

---

### Écart maximal
Crée une liste `mesures` contenant des nombres.  
Écris un programme qui calcule l’**écart maximal**, c’est-à-dire la différence entre la plus grande et la plus petite valeur, **sans utiliser `max()` ni `min()`**.

---

### Suppression d’un élément par valeur
Crée une liste `valeurs = [3, 5, 2, 5, 7, 5, 1]`.  
Demande à l’utilisateur un nombre.  
Écris un programme qui **supprime toutes les occurrences** de ce nombre dans la liste sans utiliser `remove()` ni `count()`.  
Tu pourras construire une **nouvelle liste** sans ce nombre.

---

### Décalage à gauche
Crée une liste `donnees = [10, 20, 30, 40, 50]`.  
Écris un programme qui **décale tous les éléments d’une position vers la gauche**, et place le premier élément à la fin.  
Résultat attendu : `[20, 30, 40, 50, 10]`.

---

### Fusion manuelle
Crée deux listes de nombres déjà triées dans l’ordre croissant.  
Écris un programme qui crée une **nouvelle liste triée** contenant tous les éléments des deux listes, **sans utiliser `sort()`**.  
(Indice : compare les premiers éléments de chaque liste à chaque étape.)

---

### Vérifier si la liste est triée
Crée une liste de nombres et écris un programme qui vérifie si la liste est **triée dans l’ordre croissant**.  
Le programme doit parcourir la liste et vérifier que chaque élément est inférieur ou égal au suivant.

---

### Doubles consécutifs
Crée une liste d’entiers.  
Écris un programme qui affiche **True** s’il existe au moins deux éléments identiques consécutifs, **False** sinon.  

Exemple :  
- `[1, 2, 2, 3]` → `True`  
- `[4, 5, 6, 7]` → `False`

---

### Comptage d’éléments pairs et impairs
Crée une liste d’entiers et compte combien sont pairs et combien sont impairs, **sans utiliser de compréhension ni de méthode avancée**.  
Affiche le résultat sous la forme :  

    Nombre d’éléments pairs : X
    Nombre d’éléments impairs : Y

---

### Comparaison de listes
Crée deux listes de même taille, composées d’entiers.  
Écris un programme qui compte **le nombre de positions** où les deux listes ont la **même valeur**.  

Exemple :  

    [1, 2, 3, 4]
    [1, 9, 3, 7]
    → 2 positions identiques

---

## Tableaux à deux dimensions

Une liste peut contenir d’autres listes. Cela permet de représenter des **tableaux à deux dimensions** (matrices).

```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrice[1][2])  # affiche 6
```