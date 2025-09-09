# SNT — Base de Python

Une page d’introduction pour débuter en Python : afficher du texte avec `print`, utiliser des variables (les « boîtes nommées ») et demander une saisie clavier avec `input()`.

---

## `print` — afficher dans le terminal
`print()` sert à **afficher** un message ou une valeur à l’écran (dans le terminal/console).

Quand on veut utiliser des valeurs textuelles (**chaînes de caractères**), on les écrit entre guillemets.  
Comme ça, le programme fait la différence entre le code et les chaînes de caractères.

```python
print("Bonjour")
print(2 + 3)
message = "Bienvenue en SNT !"
print(message)
```

Ce programme affichera :

    Bonjour
    5
    Bienvenue en SNT !

**Astuces**
On peut afficher **plusieurs éléments** séparés par des virgules :

```python
prenom = "Ana"
age = 15
print("Je m'appelle", prenom, "et j'ai", age, "ans.")
```

---

## Les variables — des boîtes nommées
Une **variable** est comme une **boîte** avec un **nom** dans laquelle on range une **valeur**.  
On peut lire ou **modifier** cette valeur.

```python
a = 5
b = 10
c = a + b
print(c)

a = 3
print(c)

c = a + b
print(c)
```

Ce programme affichera :

    15
    15
    13 

**Décortiquons-le :**

On a créé 3 variables.

a = 5  
b = 10  
c = a + b = 15

Puis nous avons modifié la valeur de `a` par 3, désormais, `a = 3`.  
Ce qui ne modifie pas la valeur de `c`, car ce que l'on stocke c'est la valeur et pas le calcul.  
Donc `c = 15`.

Si on veut que `c` soit de nouveau égal à `a+b`, il faut de nouveau le calculer : `c = a + b`.

---

## `input` — demander une valeur à l’utilisateur
`input()` **pose une question** et **récupère une réponse** au **format texte**.

```python
nom = input("Comment t appelles-tu ? ")
print(nom)
```

Ce programme affichera :  

    Comment t appelles-tu ?

Il faudra alors écrire notre prénom, par exemple `Tom`.  
La variable `nom` aura la valeur `"Tom"`.

Il affichera ensuite :  

    Tom

-------

En Python, **`print`** et **`input`** sont ce qu’on appelle des **fonctions**.  
Comme en mathématiques, une fonction peut **prendre des valeurs en entrée** et **renvoyer un résultat**.

**Exemple en mathématiques**
Soit la fonction : `f(x) : 2x`

- La fonction `f` prend en **entrée** une valeur `x`.  
- Elle renvoie en **sortie** le résultat du calcul `2x`.

**En Python**  
- `print(...)` prend en entrée ce que l’on veut **afficher à l’écran**.  
- `input(...)` prend en entrée un **texte à afficher** (c’est optionnel) et renvoie ce que l’utilisateur **tape au clavier**.  

On met toujours des **parenthèses** après le nom d’une fonction, même si elle n’a **aucune valeur en entrée**.  

---
## Structures de contrôle

Jusqu’ici, nous avons vu comment représenter et manipuler des nombres.  
En programmation, il est souvent nécessaire de **prendre des décisions** :  
exécuter certaines instructions seulement si une condition est vraie.  

En Python, cela se fait avec les mots-clés `if`, `elif` et `else`.

```python
if condition1:
    # instructions exécutées si la condition1 est vraie
elif condition2 :
    # instructions exécutées si la condition1 est fausse mais que la condition2 est vraie
    # on peut enchaîner plusieurs elif
else:
    # instructions exécutées si les conditions 1 et 2 sont fausses
```

On peut le lire ainsi :

- Si `condition1` est vraie, je fais ça ...  
- Sinon, si `condition2` est vraie, je fais ça ...  
- Dans tous les autre cas, je fais ça ...  
---
## Logique booléenne

### Les opérateurs logiques

Le langage Python propose trois opérateurs logiques principaux :

|Opérateur|	Syntaxe|	Signification|	Exemple|	Résultat|
|--|--|--|--|--|
|NON	|not	|inverse la valeur	|not <span style="color:blue">True</span>	|<span style="color:red">False</span>|
|ET	|and	|vrai si les deux sont vrais	|<span style="color:blue">True</span> and <span style="color:red">False</span>	|<span style="color:red">False</span>|
|OU	|or	|vrai si au moins un est vrai|	<span style="color:blue">True</span> or <span style="color:red">False</span>|	<span style="color:blue">True</span>|

Il existe aussi un opérateur important qui n'est pas naturel en python :

|OU EXCLUSIF| xor |vrai si l'un est faux et l'autre est vraie|<span style="color:blue">True</span> xor <span style="color:blue">True</span>| <span style="color:red">False</span>|
|--|--|--|--|--|

---
## Comparaisons

Les booléens apparaissent très souvent à la suite de comparaisons.  
Voici les principaux opérateurs en Python :

|Opérateur  |Signification |Exemple 1 |Résultat 1|Exemple 2|Résultat 2|
|--|--|--|--|--|--|
|==|égal à|5 == 5|<span style="color:blue">True</span>|3 = 5|<span style="color:red">False</span>|
|!=|différent de|3 != 5|<span style="color:blue">True</span>|5 != 5|<span style="color:red">False</span>|
|<|strictement inférieur|5 < 10|<span style="color:blue">True</span>|5 < 5|<span style="color:red">False</span>|
|<=|inférieur|5 <= 10|<span style="color:blue">True</span>|5 <= 5|<span style="color:blue">True</span>|
|>|strictement supérieur|5 > 10|<span style="color:red">False</span>|5 > 5|<span style="color:red">False</span>|
|>=|supérieur|5 >= 10|<span style="color:red">False</span>|5 >= 5|<span style="color:blue">True</span>|