# Révisions Python - Première

Ce document reprend les notions essentielles de Python vues en Première, avec explications, exemples et rappels importants.

---

## 1. Affichage avec `print()`

La fonction `print()` permet d’afficher du texte ou des résultats à l’écran.  
On peut afficher plusieurs éléments en les séparant par des virgules.

```python
print("Bonjour")              # affiche : Bonjour
print(3 + 5)                  # affiche : 8
print("Résultat :", 3 * 4)    # affiche : Résultat : 12
```

👉 **Astuce** : `print()` ajoute automatiquement un retour à la ligne à la fin de l’affichage.

---

## 2. Lire une valeur avec `input()`

La fonction `input()` permet de **demander une saisie à l’utilisateur**.  
Le texte entre parenthèses est un message affiché à l’écran.  

⚠️ Attention : la valeur saisie est toujours de type **chaîne de caractères** (`str`).

```python
nom = input("Quel est ton nom ? ")
print("Bonjour", nom)
```

---

## 3. Conversion avec `int()`

Si l’on veut travailler avec des nombres, il faut convertir la chaîne saisie.  
La fonction `int()` transforme une chaîne en **entier**.

```python
age = int(input("Quel est ton âge ? "))
print("Dans 10 ans tu auras", age + 10)
```

⚠️ Si l’utilisateur tape un texte qui n’est pas un nombre, `int()` provoque une erreur.

---

## 4. Les booléens (`True`, `False`)

Un **booléen** est un type de donnée qui peut avoir deux valeurs seulement :

- `True` → vrai
- `False` → faux

Ils apparaissent souvent comme résultat d’une comparaison.

```python
a = 5
b = 10
print(a < b)    # True  (car 5 est plus petit que 10)
print(a == b)   # False (car 5 n’est pas égal à 10)
print(a != b)   # True  (car 5 est différent de 10)
```

👉 On utilise beaucoup les booléens dans les conditions et les boucles.

---

## 5. Les chaînes de caractères (`str`)

Une **chaîne** est un texte entre guillemets.

```python
mot = "Python"
```

### Quelques opérations utiles :
- Accéder à une lettre : `mot[0]` → `"P"`
- Connaître la longueur : `len(mot)` → `6`
- Transformer en majuscules : `mot.upper()` → `"PYTHON"`
- Transformer en minuscules : `mot.lower()` → `"python"`

```python
print(mot[0])      # P
print(len(mot))    # 6
print(mot.upper()) # PYTHON
```

⚠️ Les indices commencent à `0` en Python.

---

## 6. Les listes

Une **liste** permet de stocker plusieurs valeurs.  
Les listes sont **modifiables** : on peut ajouter, enlever ou remplacer des éléments.

```python
fruits = ["pomme", "banane", "cerise"]

print(fruits[0])     # pomme
fruits.append("kiwi") # ajoute à la fin
print(fruits)        # ['pomme', 'banane', 'cerise', 'kiwi']

fruits[1] = "orange" # remplace "banane" par "orange"
print(fruits)        # ['pomme', 'orange', 'cerise', 'kiwi']
```

---

## 7. Les tuples

Un **tuple** ressemble à une liste, mais il est **immuable** :  
on ne peut pas modifier ses valeurs après sa création.

```python
coordonnees = (3, 5)
print(coordonnees[0])  # 3
```

👉 Les tuples sont utiles pour stocker des données fixes (exemple : une position en 2D).

---

## 8. Les conditions (`if`, `elif`, `else`)

Une condition permet de **choisir entre plusieurs actions** selon une expression booléenne.

```python
age = int(input("Ton âge ? "))

if age < 18:
    print("Tu es mineur")
elif age == 18:
    print("Tout juste majeur !")
else:
    print("Tu es majeur")
```

👉 Le mot-clé `elif` signifie « sinon si ».

---

## 9. La boucle `for`

La boucle `for` permet de **répéter une action** sur une séquence (liste, chaîne, etc.)  
ou un certain nombre de fois avec `range()`.

```python
for i in range(5):   # répète 5 fois (0 → 4)
    print("i =", i)
```

```python
fruits = ["pomme", "banane", "cerise"]
for f in fruits:
    print("J’aime", f)
```

---

## 10. La boucle `while`

La boucle `while` répète une action **tant qu’une condition est vraie**.  
⚠️ Attention : si la condition n’est jamais fausse → boucle infinie !

```python
n = 0
while n < 3:
    print("n =", n)
    n = n + 1
```

---

## 11. Les fonctions

Une **fonction** est un bloc de code réutilisable.  
On la définit avec `def`, et elle peut **renvoyer un résultat** avec `return`.

```python
def carre(x):
    return x * x

print(carre(5))   # 25
print(carre(10))  # 100
```

👉 Avantages des fonctions :
- Éviter les répétitions
- Organiser le code
- Le rendre plus lisible

---

# 📝 À retenir

- **Entrées/sorties** : `print()`, `input()`, `int()`
- **Types** : `str` (chaîne), `list` (liste modifiable), `tuple` (fixe), `bool` (vrai/faux)
- **Structures de contrôle** : `if`, `for`, `while`
- **Organisation du code** : `def` pour créer des fonctions
