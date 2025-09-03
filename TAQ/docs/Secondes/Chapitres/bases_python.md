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