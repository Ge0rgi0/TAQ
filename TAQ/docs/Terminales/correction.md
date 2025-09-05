# Correction

## Exercice 1 : Bonjour !

### Objectif
Demander le prénom de l’utilisateur et afficher un message de salutation.

### Explication pas à pas
1. `input()` lit une chaîne tapée par l’utilisateur et la renvoie.  
2. `print()` affiche du texte à l'écran. On peut afficher plusieurs éléments séparés par des virgules ; Python insère des espaces automatiquement entre eux.

### Erreurs fréquentes
- Essayer de convertir le prénom en nombre (inutile).  
- Oublier les guillemets dans le message de `input()` (pas grave mais moins clair pour l'utilisateur).

### Code corrigé

```python
# On demande le prénom à l'utilisateur et on l'affiche dans une phrase
prenom = input("Entrez votre prénom : ")   # input() renvoie une chaîne (str)
print("Bonjour,", prenom, "!")             # print concatène avec des espaces automatiques
```

### Exemple d'exécution
Si l'utilisateur tape `Alice`, le programme affiche :  
```
Bonjour, Alice !
```

---

## Exercice 2 : Opérations simples

### Objectif
Lire deux nombres et afficher leur somme, produit et différence.

### Explication pas à pas
1. `input()` renvoie une chaîne. Pour faire des opérations numériques, on convertit avec `int()` (entiers) ou `float()` (nombres à virgule).  
2. On stocke les deux nombres dans des variables `a` et `b`.  
3. On utilise les opérateurs `+`, `*`, `-` pour les calculs.  
4. `print()` affiche les résultats.

### Erreurs fréquentes
- Oublier de convertir en `int`/`float` : concaténation au lieu d'addition (ex : `'2' + '3'` donne `'23'`).  
- Conversion en `int` alors que l'utilisateur tape `3.5` (provoque `ValueError`). Si on attend des décimaux, utiliser `float()`.

### Code corrigé

```python
# Lire deux nombres et afficher les résultats
a = int(input("Entrez un premier nombre : "))   # convertir en entier
b = int(input("Entrez un deuxième nombre : "))

print("Somme :", a + b)        # addition
print("Produit :", a * b)      # multiplication
print("Différence :", a - b)   # soustraction
```

---

## Exercice 4 : Tuple et liste

### Objectif
Utiliser un tuple pour stocker des matières (fixe) et une liste pour stocker des notes (modifiable). Calculer la moyenne.

### Explication pas à pas
1. Un **tuple** est défini avec des parenthèses `(...)` et est immuable : on ne peut pas ajouter d'éléments.  
2. Une **liste** est définie avec des crochets `[...]` et on peut utiliser `append()` pour ajouter des éléments.  
3. `sum(notes)` calcule la somme des éléments d'une liste numérique. `len(notes)` donne le nombre d'éléments. La moyenne est `sum / len`.  
4. Toujours vérifier que `len(notes)` n'est pas zéro avant de diviser (éviter division par zéro).

### Erreurs fréquentes
- Tenter d'utiliser `append()` sur un tuple (provoque une erreur).  
- Diviser par zéro si la liste est vide.  

### Code corrigé

```python
# Tuple fixe pour les matières
matieres = ("Maths", "NSI", "Physique")

# Liste vide pour recueillir les notes
notes = []

# On demande 3 notes à l'utilisateur
for i in range(3):
    note = int(input("Entrez la note : "))  # on convertit en int
    notes.append(note)                              # on ajoute à la liste

# Calcul de la moyenne (on sait qu'il y a 3 notes ici)
moyenne = sum(notes) / len(notes)

print("Vos matières :", matieres)
print("Vos notes :", notes)
print("Moyenne :", moyenne)
```

---

## Exercice 5 : Boucles

### Objectif
Afficher les carrés des nombres de 1 à 10.

### Explication pas à pas
1. `range(1, 11)` génère les entiers 1,2,...,10 (le second argument est exclu).  
2. `i**2` calcule le carré de `i`.  
3. Boucler permet d'éviter d'écrire 10 lignes répétitives.

### Code corrigé

```python
for i in range(1, 11):          # parcourt 1 à 10
    print(i, "au carré =", i**2)
```

### Erreurs fréquentes
- Utiliser `range(10)` et penser que ça commence à 1 (i prendra les valeurs de 0 à 9).  
- Confondre `i*i` et `i**2` (les deux fonctionnent, mais `**` est l'opérateur d'exponentiation).

---

## Exercice 6 : Conditions

### Objectif
Classer une personne en « enfant », « adolescent » ou « adulte » selon son âge.

### Explication pas à pas
1. On lit l'âge avec `int()`.  
2. `if` teste la première condition ; si elle est vraie, Python exécute le bloc associé et saute le reste.  
3. `elif` si la première condition était fausse, teste une autre condition, si elle est vraie, Python exécute le bloc associé et saute le reste. 
4. `else` si toutes les autres conditions étaient fausses, Python exécute le bloc associé.

### Code corrigé

```python
age = int(input("Quel est ton âge ? "))

if age < 12:               # moins de 12 ans => enfant
    print("enfant")
elif age <= 17:            # entre 12 et 17 inclus => adolescent
    print("adolescent")
else:                      # 18 ans et plus => adulte
    print("adulte")
```

### Erreurs fréquentes
- Mettre les conditions dans le mauvais ordre : ici l'ordre présenté fonctionne (test du plus petit d'abord).  
- Utiliser plusieurs `if` indépendants au lieu de `elif` : cela pourrait afficher plusieurs lignes pour une même entrée.

---

## Exercice 7 : Mot de passe

### Objectif
Demander un mot de passe et répéter la demande tant qu'il est incorrect.

### Explication pas à pas
1. On utilise une boucle `while` dont la condition reste vraie tant que le mot de passe n'est pas correct.  
2. On met la saisie à l'intérieur de la boucle pour permettre plusieurs tentatives.  
3. Une fois que la condition devient fausse (mot de passe correct), la boucle s'arrête.

### Code corrigé

```python
mdp = ""                       # initialisation
while mdp != "python123":      # tant que le mot de passe n'est pas égal à la chaîne attendue
    mdp = input("Entrez le mot de passe : ")

print("Mot de passe correct !")
```

### Erreurs fréquentes
- Oublier d'initialiser `mdp` avant la boucle (la première comparaison doit être possible).  
- Utiliser `==` à l'intérieur de la boucle sans mise à jour de `mdp` (boucle infinie).

---

## Exercice 8 : Fonction simple

### Objectif
Écrire une fonction `aire_rectangle(longueur, largeur)` qui renvoie l'aire.

### Explication pas à pas
1. Une fonction est définie avec `def nom(params):`.  
2. `return` renvoie la valeur calculée à l'appelant.  
3. Pour accepter des nombres décimaux, on convertit les entrées en `float`.

### Code corrigé

```python
def aire_rectangle(longueur, largeur):
    """Retourne l'aire d'un rectangle.
    longueur et largeur sont des nombres (float ou int).
    """
    return longueur * largeur

# Lecture des valeurs utilisateur
L = float(input("Longueur : "))
l = float(input("Largeur : "))

# Appel de la fonction et affichage du résultat
print("Aire =", aire_rectangle(L, l))
```

### Erreurs fréquentes
- Oublier `return` dans la fonction (la fonction renverra `None`).  
- Convertir en `int` alors qu'on veut garder les décimales.

---

## Exercice 9 : Plus grand élément

### Objectif
Écrire `max_liste(liste)` sans utiliser la fonction `max()` intégrée.

### Explication pas à pas
1. On suppose que le premier élément est le maximum initial.  
2. On parcourt la liste et, si on trouve un élément plus grand, on met à jour `maximum`.  
3. À la fin, on retourne `maximum`.

### Erreurs fréquentes
- Oublier que la liste peut être vide. Ici on teste sur une liste connue non vide.  
- Utiliser `max()` (ici l'objectif est d'écrire la logique soi-même).

### Code corrigé

```python
def max_liste(liste):
    # On suppose que la liste contient au moins un élément
    maximum = liste[0]
    for element in liste:
        if element > maximum:
            maximum = element
    return maximum

# Exemple de test
nombres = [3, 17, 9, 25, 4]
print("Liste :", nombres)
print("Plus grand élément :", max_liste(nombres))
```

---

## Exercice 10 : Petit projet

### Objectif
Lire des notes jusqu'à ce que l'utilisateur tape `-1`, puis afficher la liste, la moyenne et le nombre de notes >= moyenne.

### Explication pas à pas
1. On crée une liste `notes` vide.  
2. On lit des notes dans une boucle `while` jusqu'à la valeur sentinelle `-1`.  
3. On n'ajoute `-1` **pas** à la liste (contrôle nécessaire).  
4. Si la liste est non vide, on calcule `moyenne = sum(notes) / len(notes)`.  
5. On parcourt la liste pour compter les éléments supérieurs ou égaux à la moyenne.

### Erreurs fréquentes
- Oublier d'exclure `-1` (alors la moyenne est faussée).  
- Tenter de calculer la moyenne sur une liste vide (division par zéro).  

### Code corrigé

```python
notes = []
note = 0  # valeur initiale (autre que -1)

# Lecture des notes
while note != -1:
    # On convertit en int ; si l'utilisateur tape une valeur non numérique, il y aura une erreur
    note = int(input("Entrez une note (-1 pour arrêter) : "))
    if note != -1:
        notes.append(note)  # on n'ajoute pas -1

# Affichage des notes saisies
print("Toutes les notes :", notes)

# Calculs seulement si la liste contient au moins une note
if len(notes) > 0:
    moyenne = sum(notes) / len(notes)
    print("Moyenne :", moyenne)

    # Compter les notes >= moyenne
    nb_sup = 0
    for n in notes:
        if n >= moyenne:
            nb_sup += 1

    print("Nombre de notes >= moyenne :", nb_sup)
else:
    print("Aucune note entrée.")
```

### Remarque
- Si tu veux ignorer les notes invalides (ex : négatives, supérieures à 20), ajoute des vérifications avant `append()`.
- On pourrait aussi afficher la médiane, l'écart-type, etc., mais cela dépasse l'exercice.
