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

|Avant|Après|
|-|-|
|["pomme", "banane", "cerise"]|["pomme", "banane", "cerise", <span style="color:green">"orange"</span>]|

### Suppression d’un élément
```python
fruits.remove("banane")
```
|Avant|Après|
|-|-|
|["pomme", <span style="color:red">"banane"</span>, "cerise","orange"]|["pomme", "cerise","orange"]|

### Modification d’un élément
```python
fruits[0] = "kiwi"
```

|Avant|Après|
|-|-|
|[<span style="color:red">"pomme"</span>, "cerise","orange"]|[<span style="color:green">"kiwi"</span>, "cerise","orange"]|

### Taille du tableau
```python
print(len(fruits))  # nombre d'éléments
```

### Présence d'un élément
```python
l = [1,2,3]
print(1 in l) # True
print(4 in l) # False
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

Affichera : 

```
kiwi
cerise
orange
```

### Avec les indices
```python
for i in range(len(fruits)):
    print("Indice", i, ":", fruits[i])
```

Affichera :

```
Indice 0 : kiwi
Indice 1 : cerise
Indice 2 : orange
```

### Exemple d'utilisation

```python
# Ce programme calcul la moyenne d'une liste de notes

notes = [10, 15, 12, 8, 17]
somme = 0
for note in notes:
    somme += note

m = somme / len(notes)
print(m)
```

---

## Les tranches

En Python, un **slice** permet d’extraire une portion d’une séquence.

La syntaxe générale est : `nom_de_la_liste[debut : fin]`

- debut correspond à l'indice du premier élément que l'on veut prendre (si on le l'indique pas, on commencera à l'indice 0)
- fin correspond à l'indice du premier élément que l'on ne veut peux plus (si on ne l'indique pas, on ira juqu'au dernier indice)

`liste[1:5]` crée une nouvelle liste avec les éléments de *liste* en partant de l'indice 1 à 4 (inclus).

exemples :
```

liste = [0,1,2,3,4,5,6,7,8,9,10]

print(liste[1:5]) # [1,2,3,4]

print(liste(5:)) # [5,6,7,8,9,10]

print(liste(:5)) # [0,1,2,3,4]

```

On peut également ajouter un **pas**.
On utilise alors la syntaxe : `nom_de_la_liste[debut : fin : pas]`
ou bien : `nom_de_la_liste [::pas]` si on ne veut indiquer que le pas

- pas indique de combien on avance dans la liste à chaque étape
- si le pas est négatif, on parcourt la liste à l’envers

exemple :
```

print(liste[::2]) # prendre un élément sur deux [0, 2, 4, 6, 8, 10]

print(liste[::3])  # prendre un élément sur trois [0, 3, 6, 9]

print(liste[1::2])  # prendre un élément sur deux en commençant à l’indice 1 [1, 3, 5, 7, 9]

print(liste[::-1])  # à l'envers [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(liste[::-2])  # à l’envers en prenant un élément sur deux [10, 8, 6, 4, 2, 0]

print(liste[2:9:2])  # [2, 4, 6, 8]

print(liste[8:2:-1])  # [8, 7, 6, 5, 4, 3]

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

### Final
Crée une liste vide. Tant que l'utilisateur rentre des valeurs, on les ajouter à notre liste. 

- Si la valeur que nous souhaitons ajouter est deja présente, on retire l'autre occurence.  
- Si l'utilisateur entre la valeur `0`, le programme affiche la liste et s'arrête.

---

## Liste à deux dimensions (Matrices)

En Python, une liste peut contenir d’autres listes.
On parle alors de tableau à deux dimensions, ou matrice.

```Python
matrice = [
    [1, 2, 3],   # ligne 0
    [4, 5, 6],   # ligne 1
    [7, 8, 9]    # ligne 2
]
```

Pour accéder à un élément, il faut deux indices :

- le premier : numéro de la ligne
- le second : numéro de la colonne

```Python
print(matrice[1][2])  # affiche 6
```

<span style="color:red">Exercices :</span>  

### Affichage formaté

Créer une matrice 3×3 et l’afficher sous forme de grille :

```
1  2  3  
4  5  6  
7  8  9
```

---

### Somme des éléments

Écris un programme qui affiche la somme de tous les éléments de cette matrice.

---

### Recherche dans un tableau 2D

Demander un nombre à l’utilisateur et vérifier s’il est présent dans la matrice (sans utiliser `in`).

---

### Maximum et minimum

Trouver le plus grand et le plus petit élément (sans max() ni min()) de la matrice.

---

### Transposer une matrice

Construire une fonction qui prend en paramètre une matrice et qui en renvoit une nouvelle où les lignes sont devenus les colonnes.

Exemple :
```
1  2  3        1  4  7
4  5  6   ->   2  5  8
7  8  9        3  6  9
```

---

## Listes par compréhension

Les listes par compréhension sont une manière rapide et élégante de créer des listes à partir d’une autre liste.

Elles permettent :

- de transformer les valeurs
- de filtrer certaines valeurs
- de créer directement des tableaux 2D

Elles remplacent souvent une boucle simple.

**Syntaxe générale**

[expression for element in tuple/liste/range if condition]

- expression : ce que l’on met dans la nouvelle liste
- element : variable qui prend chaque valeur
- condition (facultative) : filtre les éléments

**Exemples simples**

- **Doubler chaque nombre**  
nombres = [1, 2, 3, 4]  
doubles = [x * 2 for x in nombres]  
`[2, 4, 6, 8]`  

- **Garder uniquement les nombres pairs**  
pairs = [x for x in nombres if x % 2 == 0]  
`[2, 4]`  

- **Lire les lettres d’une chaîne**  
mot = "bonjour"  
lettres = [c for c in mot]  
`['b', 'o', 'n', 'j', 'o', 'u', 'r']`  

**Listes par compréhension imbriquées**

Les compréhensions peuvent créer des matrices :

matrice = [[i * j for j in range(5)] for i in range(5)]

```
[[0, 0, 0, 0, 0],
[0, 1, 2, 3, 4],
[0, 2, 4, 6, 8],
[0, 3, 6, 9, 12],
[0, 4, 8, 12, 16]]

```

<span style="color:red">Exercices :</span>  

**Doubles**

Créer une liste contenant chaque élément d’une liste donnée divisés par 2.

**Filtrer les nombres**

Créer une liste contenant uniquement les nombres strictement supérieurs à 10 et inférieur à 20.

**Carrés**

Créer une liste contenant les carrés des entiers de 1 à 20.

**Lettres sans voyelles**

À partir d’un mot, créer une liste contenant uniquement ses consonnes.

**Matrice identité 5×5**

Créer une matrice de taille 5 où les diagonales valent 1 et le reste 0.

**Produit de deux listes**

Étant données deux listes A et B, créer la liste de tous les produits a*b.

```
a = [1, 2]  ->  2 3
b = [2, 3]      4 6
```