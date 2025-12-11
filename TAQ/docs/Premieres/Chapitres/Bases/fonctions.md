# Les fonctions Python

Une fonction est un bloc de code réutilisable qui réalise une tâche
précise.  

Elle permet : 

- d'éviter les répétitions, 
- de rendre le code plus lisible, 
- de structurer un programme en sous‑problèmes.

------------------------------------------------------------------------

## Définir et appeler une fonction

En Python, on définit une fonction avec le mot clé `def`. Lors de la définition, le nom de la fonction doit toujours être suivi par des parenthèses.

Quand une fonction termine son travail, elle peut renvoyer un résultat.  
Ce résultat est appelé valeur de retour et est précédée par le mot clé `return`.  

``` python
def nom_de_la_fonction():
    # bloc d’instructions
    return resultat
```

Une fois définie, on peut l'utiliser autant de fois que nécessaire, on dit que l'on appelle la fonction, pour cela il suffit d'écrire le nom de la fonction (toujours suivi de parenthéses).

La valeur renvoyée peut alors être utilisée :

``` python
print(nom_de_la_fonction())
```

ou bien stockée dans une variable pour s'en servir plus tard :

``` python
variable = nom_de_la_fonction()
...
print(variable)
```

### Aucune valeur de retour

Une fonction peut ne rien renvoyer (pas de `return`).  
Python renvoie alors automatiquement la valeur : `None`.

``` python
def afficher(x):
    print(x)
```

Cette fonction affiche un résultat mais ne revoie rien.

### Placement du return

Quand l'instruction `return` est effectuée l'execution de la fonction s'arrête. Toutes les instructions qui suivent ne seront donc pas exécutée.

```Python

def f1():
  ...
  return ...
  # bloc d'instructions jamais exécuté

def f2():
  ...
  if ... :
    ...
    return ...
    # bloc d'instructions jamais exécuté

  else :
    ...
    return ...
    # bloc d'instructions jamais exécuté

```

------------------------------------------------------------------------

## Paramètres et arguments

Lorsqu’on utilise une fonction, on distingue deux notions importantes : les paramètres et les arguments.  
Elles se ressemblent, mais leur rôle est différent.

Les **paramètres** sont les variables écrites dans la définition de la fonction.
Alors que les **arguments** sont les valeurs envoyées lors de l'appel.

``` python
def addition(a, b):  # a et b sont des paramètres
    return a + b

print(addition(3, 5))  # 3 et 5 sont des arguments
```

Dans cette fonction, `a` prendra la valeur `3`, et `b` la valeur `5`.

**Fonction sans paramètre**

Une fonction ne nécessite pas forcement de paramètre, exemple :

``` python
def bonjour():
    print("Bonjour !")
```

**Paramètres par défaut**

On peut donner une valeur par défaut à un paramètre, qui sera utilisée si aucun argument n’est fourni.

```python
def saluer(nom="élève"):
    print("Bonjour", nom)

saluer()        # Bonjour élève
saluer("Alice") # Bonjour Alice

```

------------------------------------------------------------------------

## Portée des variables

-   Une variable définie **dans** une fonction est **locale**.
-   Les variables définies **hors** d'une fonction sont **globales**.

Une variable globale est accessible dans une fonction (si elle est définie avant l'appel).  
Une variable locale n'est pas accessible en dehors de la définition de la fonction.

``` python
x = 10  # variable globale

def f():
    y = 5  # variable locale
    print(y)

f()
print(x)
```

------------------------------------------------------------------------

## Exemple complet

``` python
def moyenne(notes):
    '''
    Renvoie la moyenne d’une liste de notes.
    '''
    total = sum(notes)
    return total / len(notes)

eleve = [15, 12, 18]
print("Moyenne :", moyenne(eleve))
```

-------------

## Exercices de découverte

### Fonction simple
Écris une fonction `salutation()` qui affiche `Salut !`  
Appelle-la deux fois.

---

### Fonction avec paramètre
Écris une fonction `accueil(prenom)` qui affiche `Salut <prenom> !`  

---

### Fonction avec paramètre par défaut
Écris une fonction `accueil_defaut(prenom="ami")`  
Teste avec et sans argument.


### Carré d’un nombre
Écris une fonction `puissance2(nombre)` qui renvoie le carré d’un nombre.  

---

### Somme de deux nombres
Écris une fonction `somme(a, b)` qui renvoie la somme.  

---

### Moyenne de trois nombres
Écris une fonction `calcul_moyenne(x, y, z)` qui renvoie la moyenne.  

---

### Affichage multiple
Écris une fonction `repeter_mot(mot, n)` qui affiche le mot `mot` `n` fois, sans `return`.


### Comparaison
Écris une fonction `plus_grand(a, b)` qui renvoie le plus grand des deux nombres.  

---

### Vérifier si pair
Écris une fonction `est_pair(n)` qui renvoie `True` si `n` est pair, sinon `False`.  

---

## Exercices avancés


### Exercice 1 : Somme des carrés
Écris une fonction `somme_carres(a, b)` qui renvoie la somme des carrés des deux nombres `a` et `b`.  
Exemple : `somme_carres(3, 4)` → `25`.

---

### Exercice 2 : Comparaison chaînes
Écris une fonction `plus_long(s1, s2)` qui renvoie la chaîne la plus longue entre `s1` et `s2`.  
Si elles sont de même longueur, renvoie `"Égal"`.

---

### Exercice 3 : Maximum de trois nombres
Écris une fonction `max3(a, b, c)` qui renvoie le plus grand des trois nombres **sans utiliser de listes**.  

---

### Exercice 4 : Conversion heures/minutes
Écris une fonction `convertir_minutes(heures, minutes)` qui renvoie le total en minutes.  
Exemple : `(2, 30)` → `150`.

---

### Exercice 5 : Table de multiplication
Écris une fonction `table(n)` qui affiche la table de multiplication de `n` jusqu’à 10.  

---

### Exercice 6 : Vérifier palindrome
Écris une fonction `est_palindrome(s)` qui renvoie `True` si la chaîne `s` est un palindrome, sinon `False`.  
Exemple : `"radar"` → `True`, `"python"` → `False`.

---

### Exercice 7 : Compter les chiffres d’un nombre
Écris une fonction `nb_chiffres(n)` qui renvoie le nombre de chiffres dans un nombre entier positif.  
Exemple : `nb_chiffres(12345)` → `5`.