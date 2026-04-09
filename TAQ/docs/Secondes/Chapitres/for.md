# Les boucles `for` en Python

---

## 1. C'est quoi une boucle ?

Imagine que tu dois écrire 5 fois "Bonjour !" à la main :

```python
print("Bonjour !")
print("Bonjour !")
print("Bonjour !")
print("Bonjour !")
print("Bonjour !")
```

C'est répétitif. Et si tu devais le faire 1000 fois ? Une **boucle** permet de répéter automatiquement des instructions autant de fois qu'on le souhaite.

---

## 2. La boucle `for` avec `loop`

En Python, on écrit une boucle `for` de cette façon :

```python
for loop in range(5):
    print("Bonjour !")
```

**Résultat :**
```
Bonjour !
Bonjour !
Bonjour !
Bonjour !
Bonjour !
```

- `for` démarre la boucle
- `loop` est la variable de boucle (on verra son utilité plus tard)
- `range(5)` indique qu'on fait 5 tours
- `:` est obligatoire à la fin de la ligne `for`
- La ligne du dessous est **indentée** (décalée) : c'est elle qui est répétée

La variable `loop` prend une nouvelle valeur à chaque tour. On peut l'afficher :

---

## 3. L'indentation : la règle la plus importante

En Python, l'indentation (le décalage vers la droite d'une ligne) **définit ce qui est à l'intérieur de la boucle**.

Tout ce qui est indenté après le `for` sera répété à chaque tour.  
Tout ce qui ne l'est pas s'exécute une seule fois, après la fin de la boucle.

### Une seule ligne indentée

```python
for loop in range(3):
    print("Je suis dans la boucle")
print("Je suis en dehors de la boucle")
```

**Résultat :**
```
Je suis dans la boucle
Je suis dans la boucle
Je suis dans la boucle
Je suis en dehors de la boucle
```

Le dernier `print` n'est pas décalé : il ne s'exécute qu'une seule fois, après les 3 tours.

---

### Plusieurs lignes indentées

On peut mettre autant de lignes qu'on veut à l'intérieur d'une boucle :

```python
for loop in range(3):
    print("Je suis toujours dans la boucle")
    print("Moi aussi")
print("La boucle est terminee")
```

**Résultat :**
```
Je suis toujours dans la boucle
Moi aussi
Je suis toujours dans la boucle
Moi aussi
Je suis toujours dans la boucle
Moi aussi
La boucle est terminee
```

Les deux premiers `print` sont indentés : ils se répètent 3 fois.  
Le dernier ne l'est pas : il ne s'exécute qu'une fois.

---

### Avant, pendant, après

```python
print("Avant la boucle")

for loop in range(4):
    print("Debut du tour")
    print("Fin du tour")

print("Apres la boucle")
```

**Résultat :**
```
Avant la boucle
Debut du tour
Fin du tour
Debut du tour
Fin du tour
Debut du tour
Fin du tour
Debut du tour
Fin du tour
Apres la boucle
```

---

### L'indentation change tout au résultat

Observe bien la différence entre ces deux programmes qui ne différent que par l'indentation d'une ligne :

**Programme A — le `print` est dans la boucle :**
```python
total = 0
for loop in range(5):
    total = total + 1
    print("Total :", total)
```

**Résultat A :**
```
Total : 1
Total : 2
Total : 3
Total : 4
Total : 5
```

**Programme B — le `print` est en dehors de la boucle :**
```python
total = 0
for loop in range(5):
    total = total + 1
print("Total :", total)
```

**Résultat B :**
```
Total : 5
```

Un seul espace de différence, et le résultat est complètement différent.

---

### L'erreur classique : oublier l'indentation

```python
for loop in range(3):
print("Bonjour")   # ERREUR : cette ligne n'est pas indentée
```

Python retourne immédiatement une erreur : `IndentationError: expected an indented block`. Il faut toujours indenter au moins une ligne à l'intérieur d'une boucle.

---

## 4. Utiliser `loop` pour faire des calculs
 
La variable de boucle (`loop` dans notre cas) est une véritable variable qui évolue au fur et à mesure des tours.
 
```python
for loop in range(5):
    print(loop)
```
 
**Résultat :**
```
0
1
2
3
4
```
 
On remarque que l'on affiche bien 5 valeurs, mais puisque l'on commence à 0 on s'arrêtera à 4.
 
---
 
### `range()` avec deux valeurs : choisir la valeur de départ
 
Pour ne pas démarrer à 0, on peut donner deux valeurs à `range()` : un début et une fin.
 
```python
for loop in range(1, 6):
    print(loop)
```
 
**Résultat :**
```
1
2
3
4
5
```
 
La syntaxe est `range(début, fin)`.
La valeur de fin n'est **jamais atteinte** : ici `range(1, 6)` s'arrête à 5.
 
```python
for loop in range(3, 8):
    print(loop)
```
 
**Résultat :**
```
3
4
5
6
7
```
 
---
 
### `range()` avec trois valeurs : choisir le pas
 
On peut aussi indiquer un **pas**, c'est-à-dire de combien `loop` avance à chaque tour. La syntaxe devient `range(début, fin, pas)`.
 
```python
for loop in range(0, 20, 5):
    print(loop)
```
 
**Résultat :**
```
0
5
10
15
```
 
On avance de 5 en 5. La valeur 20 n'est pas atteinte.
 
```python
for loop in range(0, 11, 2):
    print(loop)
```
 
**Résultat :**
```
0
2
4
6
8
10
```
 
On avance de 2 en 2 : on obtient tous les nombres pairs entre 0 et 10.
 
Le pas peut aussi être **négatif** pour compter à rebours. Dans ce cas, le début doit être plus grand que la fin :
 
```python
for loop in range(5, 0, -1):
    print(loop)
```
 
**Résultat :**
```
5
4
3
2
1
```
 
On avance de -1 en -1, la valeur 0 n'est jamais atteinte.
 
---
 
## 5. Les boucles imbriquées
 
On peut placer une boucle à l'intérieur d'une autre boucle. On parle alors de boucles **imbriquées**. L'indentation prend alors encore plus d'importance : il y a deux niveaux.
 
```python
for loop in range(2):
    print("a")
    for loop2 in range(3):
        print("b")
    print("c")
 
print("d")
```
 
**Résultat :**
```
a
b
b
b
c
a
b
b
b
c
d
```
 
### Exemple : dessiner un rectangle
 
```python
for loop in range(4):
    for loop2 in range(6):
        print("*", end="")
    print()
```
 
**Résultat :**
```
******
******
******
******
```
 
- La boucle extérieure gère les lignes (4 lignes)
- La boucle intérieure gère les colonnes (6 étoiles par ligne)
- `print()` est indenté d'un seul niveau : il s'exécute après chaque ligne complète pour passer à la suivante
 
---
 
## 6. Les erreurs fréquentes
 
| Erreur | Conséquence | Correction |
|---|---|---|
| Oublier `:` après `for loop in range(...)` | `SyntaxError` | Toujours mettre `:` |
| Ne pas indenter le bloc | `IndentationError` | Décaler de 4 espaces |
| Mal indenter une ligne | Le programme tourne mais donne un mauvais résultat | Vérifier chaque niveau d'indentation |
| Utiliser le même nom pour deux boucles imbriquées | La variable extérieure est écrasée | Utiliser `loop` et `loop2` |
 
---
 
## Exercices
 
1. Affiche 10 fois la phrase "Python c'est bien".
2. Affiche les nombres de 1 à 20. Pour chaque nombre, indique s'il est pair ou impair. A la fin, affiche "Fin du programme".
3. Calcule et affiche la somme des entiers de 1 à 100. Affiche uniquement le résultat final.
4. Affiche un triangle d'étoiles de 5 lignes (1 étoile sur la premiere ligne, 2 sur la deuxieme, etc.) en utilisant des boucles imbriquées.
5. Affiche les tables de multiplication de 1 à 5 (de 1 à 10 pour chaque table). Entre chaque table, affiche une ligne de séparation.