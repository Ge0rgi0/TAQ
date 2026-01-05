# Notions algorithmiques

## Introduction

L’algorithmique étudie les méthodes permettant de résoudre un problème de manière
systématique. Un **algorithme** est une suite d’instructions permettant d’obtenir un
résultat à partir d’entrées données.

Dans ce chapitre, nous étudions un algorithme classique : **la recherche séquentielle**.  
Il nous servira d’exemple pour introduire :

- la notion de **spécification** 
- la **correction** d’un algorithme 
- la notion d’**invariant** 
- la **terminaison** 
- la **complexité** temporelle.

---

## La recherche séquentielle

On souhaite savoir si une valeur `x` est présente dans une liste `t`.  
L’idée de la recherche séquentielle est simple :

> On examine les éléments de la liste un par un, dans l’ordre, jusqu’à trouver la valeur recherchée (ou pas).

**Exemple**

Liste : `[4, 7, 2, 9]`  
Valeur recherchée : `9`

On compare successivement :

- 4 ≠ 9  
- 7 ≠ 9
- 2 ≠ 9
- 9 = 9 → trouvé

L'algorithme de la recherche séquentielle en python :
```python
def recherche_sequentielle(t, x):
    for e in t :
        if e == x :
            return True
    return False
```

---

## Spécifier un algorithme

### Les types

La première étape pour étudier un algorithme consiste à définir précisément ce qu’il est censé faire.

Pour commencer nous pouvons préciser de quels types sont les paramètres ainsi que les valeurs de retour :

```python
def recherche_sequentielle(t : list[any], x : any) -> bool:
    for e in t :
        if e == x :
            return True
    return False
```

Les noms des types sont les suivants : ``int``, `float`, ``bool``, ``str``, ``tuple``, ``list``, ``dict``, ``None``, ...  

Le type `any` précise que cette valeur peut être de n’importe quel type.

Quelques exemples concernant :

- les tuples : `tuple`, `tuple[int]`, `tuple[int, str]`, ``(int)``
- les listes : `list`, `list[int]`, `[int]`, `list[list[int]]`
- les dictionnaires : `dict`, `dict[str : int]`

### Documentation

Une ``docstring`` est un texte placé juste sous la définition d’une fonction (ou d’une classe) qui explique son rôle, ses paramètres et sa valeur de retour.  
En Python, c’est le moyen officiel de documenter du code.

```python
def recherche_sequentielle(t : list, x : any) -> bool:
    """
    Renvoie True si x est présent dans la liste L, False sinon.
    """
    for e in t :
        if e == x :
            return True
    return False
```

---

## Correction de l’algorithme

Un algorithme est correct s’il réalise exactement ce que dit sa spécification.

### Invariant de boucle

Pour prouver la correction, on utilise un invariant : une propriété qui reste vraie pendant toute l’exécution d’une boucle, à chaque itération.
C’est un outil essentiel en algorithmique pour montrer qu’un programme est correct, c’est-à-dire qu’il fait bien ce qu’il est censé faire.

> Avant chaque itération de la boucle for, tous les éléments déjà parcourus dans la liste ont été testés et aucun n’est égal à x.

Autrement dit, tant que l’on continue la boucle, on est sûr que :

- x n’a pas été trouvé dans les éléments déjà examinés ;
- s’il apparaît dans la liste, il ne peut être que dans les éléments restants à parcourir.

Cet invariant reste vrai :

- au début de la boucle ;
- après chaque itération ;
- jusqu’à la fin.

Quand la boucle se termine, si rien n’a été trouvé, alors `x` n’est pas dans ``L``, et l’algorithme renvoie `False`.  
S’il est trouvé en cours de route, l’algorithme renvoie `True`.

>On ne vous demandera pas de prouver la correction d'un algorithme au **bac**.  
>Cependant il est possible que l'on vous demande de trouver un invariant correct.

---

## Terminaison

L’algorithme doit garantir qu’il se termine toujours.  
La terminaison repose sur un variant de boucle : **le nombre d’éléments restants à parcourir**.

### Boucle `for`

Concernant les boucles `for`, il n'est pas nécessaire de prouver que ce soit. Il faut simplement retenir et rappeler qu'une boucle `for` (c'est à dire une boucle bornée) se termine toujours.

À chaque itération :

- on avance d’un élément dans la liste,  
- donc ce nombre diminue,  
- et finit à 0.

La boucle bornée se termine donc forcément.

### Boucle `while`

Contrairement à une boucle for, une boucle while n’est pas automatiquement terminante.  
Il faut donc montrer qu’elle s’arrête, en utilisant un variant de boucle.

Un variant est une valeur :  

- entière  
- positive ou au moins bornée inférieurement  
- qui diminue strictement à chaque itération

Si cette valeur ne peut pas descendre indéfiniment, alors la boucle doit terminer.

Voici notre même algorithme, cette fois écrit avecc une boucle non bornée.

```python
def recherche_sequentielle(t, x):
    i = 0
    while i < len(t):
        if t[i] == x:
            return True
        i = i + 1
    return False
```

Variant possible : ``len(t) - i``

- Au début, il vaut ``len(t)`` (toujour strictement positif)
- À chaque tour, ``i`` augmente de ``1`` ⇒ ``len(t) - i`` diminue strictement
- Il devient ``0`` lorsque ``i == len(t)``

Il ne peut pas devenir négatif ⇒ la boucle ne peut pas tourner indéfiniment.  
Donc la boucle se termine toujours.

Cette preuve repose sur le même principe que celui des preuves par réccurence en mathématique.

---

## Complexité

La complexité mesure le coût d’un algorithme (temps, mémoire…).  
Nous étudions ici la complexité temporelle.

L'interêt de ce genre de mesure est multiple :
- comparer deux algorithmes qui résolvent le même problème (on veut des algorithmes rapides)
- anticiper si un programme restera rapide quand on augmente la taille des données
- choisir la bonne méthode selon le contexte (données nombreuses, contraintes de temps…)

La complexité donne donc une idée de l’évolution du temps d’exécution en fonction de la taille n de l’entrée.

Pour l'estimer on cherche quel serait le pire scénario (celui où l'éxecution serait la plus longue, par exemple pour la recherche séquentielle ce serait que l'élément recherché ne soit pas dans la liste ou bien uniquement à la dernière place).
On calcule le nombre de tour de boucle nécessaire à son exécution puis nous ne regardons que l'ordre de grandeur.

![](time-complexity.png)

Voici les ordres les plus courants :

**O(1) : temps constant**

Le temps ne dépend pas de la taille des données.
Exemples : accéder à un élément d’une liste par son index, affecter une variable.

Exemple : 
```python
def f(a,b):
    return a + b

```

**O(log n) : logarithmique**

Très rapide même pour de grandes valeurs. Le temps augmente très lentement.
Exemple : recherche dichotomique (en terminale).

**O(n) : linéaire**

Le temps augmente proportionnellement à n.
Exemple : parcourir une liste du début à la fin.

Exemple : 
```python
def f(t):
    s = 0
    for e in t :
        s += e
    return s
```

**O(n log n)**

Typique des algorithmes de tri efficaces (terminal).
Rapide même pour de grandes données.

**O(n²) : quadratique**

Beaucoup plus lent ; augmente très vite.

```python
def f(t):
    res = []
    for i in t:
        for j in t:
            res.append(i*j)
    return res
```

**O(2ⁿ), O(n!)**

Très coûteux. Impraticables pour n un peu grand.
On ne les rencontre pas en classe, sauf pour montrer qu’ils sont impossibles à utiliser.

## Exercice

## Exercices : approfondir les notions algorithmiques

Les exercices suivants permettent de s’entraîner à :
- écrire une spécification claire,
- identifier un invariant de boucle,
- justifier la terminaison à l’aide d’un variant,
- estimer la complexité temporelle.

---

### Exercice 1 — Test d’appartenance borné

Écrire une fonction `contient_jusqua(t, x, k)` qui renvoie `True` si la valeur `x`
est présente dans les `k` premiers éléments de la liste `t`, et `False` sinon.

Contraintes :
- on suppose que `0 ≤ k ≤ len(t)`.

Questions :
1. Donner une spécification (types + docstring).
2. Proposer un invariant de boucle.
3. Identifier un variant si une boucle `while` est utilisée.
4. Donner la complexité dans le pire cas.

---

### Exercice 2 — Compter des occurrences

Écrire une fonction `compte(t, x)` qui renvoie le nombre de fois où `x`
apparaît dans la liste `t`.

Questions :
1. Quel est l’invariant de la boucle ?
2. Pourquoi l’algorithme est-il correct ?
3. Donner la complexité temporelle.

Indication : on parcourt toute la liste, même si `x` est trouvé rapidement.

---

### Exercice 3 — Recherche avec arrêt anticipé

On suppose que la liste `t` est triée dans l’ordre croissant.

Écrire une fonction `recherche_ordonnee(t, x)` qui :
- parcourt la liste,
- s’arrête dès que l’élément courant est strictement supérieur à `x`.

Questions :
1. Quelle est la spécification ?
2. Proposer un invariant.
3. Dans quels cas l’algorithme est-il plus rapide que la recherche séquentielle classique ?
4. Donner la complexité dans le pire cas et dans le meilleur cas.

---

### Exercice 4 — Minimum d’une liste (boucle while)

Écrire une fonction `minimum(t)` qui renvoie la plus petite valeur de la liste `t`.

Contraintes :
- la liste contient au moins un élément,
- utiliser une boucle `while`.

Questions :
1. Donner le variant de boucle.
2. Formuler un invariant expliquant pourquoi le minimum trouvé est correct.
3. Donner la complexité temporelle.

---

### Exercice 5 — Somme partielle

Écrire une fonction `somme_jusqua(t, k)` qui renvoie la somme des `k`
premiers éléments de la liste `t`.

Questions :
1. Donner la spécification complète.
2. Proposer un invariant.
3. Quelle est la complexité en fonction de `k` ?

---

### Exercice 6 — Vérifier si une liste est croissante

Écrire une fonction `est_croissante(t)` qui renvoie `True` si la liste est
triée dans l’ordre croissant, et `False` sinon.

Questions :
1. Quel invariant permet d’expliquer la correction ?
2. Pourquoi la fonction peut-elle s’arrêter avant la fin de la liste ?
3. Donner la complexité dans le pire cas.

---

### Exercice 7 — Produit de deux listes (double boucle)

Écrire une fonction `produit(t1, t2)` qui affiche tous les produits `a × b`
avec `a` dans `t1` et `b` dans `t2`.

Questions :
1. Donner la complexité en fonction de `n = len(t1)` et `m = len(t2)`.
2. Pourquoi la complexité devient-elle quadratique si `n = m` ?
3. Existe-t-il un invariant utile ici ? Pourquoi (ou pourquoi pas) ?
