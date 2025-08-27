# Bases de Python

## Introduction
Python est le langage choisi pour l’enseignement de la spécialité NSI.  

Pourquoi Python ?  
- Il est **simple** d’écriture et de lecture.  
- Il est **libre et gratuit**, disponible sur toutes les plateformes.  
- Il est **interprété** : pas besoin de compilation, on peut tester rapidement son code.  
- Il possède de nombreuses **bibliothèques** utiles en mathématiques, sciences, économie, etc.  

---

## 1. Variables et affectations

Une **variable** permet de stocker une valeur en mémoire.  
L’opération qui associe une valeur à une variable s’appelle une **affectation**.  

```python
x = 5
y = 3
z = x + y
print(z)  # affiche z
```

👉 Ici, `x` et `y` contiennent des entiers, et `z` reçoit la somme.  

⚠️ En Python, le signe `=` n’a pas le même sens qu’en mathématiques : il signifie **« prend la valeur »**.  

**Exercice**  
- Affecter la valeur 2025 à une variable `annee`, puis afficher `annee + 10`.  

---

## 2. Séquences (chaînes, listes)

Une **séquence** est une collection ordonnée d’éléments.  
Les deux séquences principales en Python sont :  

- La **chaîne de caractères** (`str`)  

```python
nom = "Python"
print(nom[0])   # affiche 'P'
print(len(nom)) # affiche 6
```

- La **liste** (`list`)  

```python
notes = [15, 12, 18]
print(notes[1])     # affiche 12
notes.append(14)    # ajoute 14 à la liste
```

**Exercice**  
Créer une liste contenant trois prénoms et afficher le deuxième.  

---

## 3. Instructions conditionnelles

Elles permettent d’**exécuter du code seulement si une condition est vraie**.  

```python
age = 17

if age >= 18:
    print("Majeur")
else:
    print("Mineur")
```

On peut ajouter plusieurs cas avec `elif`.  

```python
note = 15

if note >= 16:
    print("Très bien")
elif note >= 12:
    print("Assez bien")
else:
    print("À améliorer")
```

**Exercice**  
Demander à l’utilisateur son âge avec `input()`, puis afficher :  
- « Mineur » si l’âge est < 18  
- « Majeur » sinon  

---

## 4. Boucles

Les boucles permettent de **répéter des instructions**.  

- **Boucle bornée** : on connaît à l’avance le nombre de répétitions.  

```python
for i in range(5):
    print("Bonjour", i)
```

- **Boucle non bornée** : on répète tant qu’une condition est vraie.  

```python
n = 0
while n < 5:
    print("n =", n)
    n = n + 1
```

**Exercice**  
Écrire un programme qui affiche les entiers de 1 à 10 avec une boucle `while`.  

---

## 5. Fonctions

Une **fonction** permet de regrouper un ensemble d’instructions sous un nom.  
On peut ensuite l’**appeler** autant de fois que nécessaire.  

```python
def carre(x):
    return x * x

print(carre(5))   # affiche 25
```

👉 `def` sert à définir la fonction. `return` renvoie le résultat.  

**Exercice**  
Écrire une fonction `aire_rectangle(longueur, largeur)` qui renvoie l’aire du rectangle.  
Tester avec plusieurs valeurs.  

---

## Conclusion

Avec ces bases (variables, séquences, conditions, boucles, fonctions), on peut déjà :  
- résoudre des problèmes concrets,  
- modéliser des phénomènes,  
- écrire des programmes utiles et réutilisables.  

C’est la fondation de l’apprentissage en NSI.
