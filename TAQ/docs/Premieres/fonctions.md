# Cours : Les fonctions en Python

## 1. Pourquoi utiliser des fonctions ?

Imagine un programme qui doit calculer plusieurs fois une même opération (par exemple, le périmètre d’un rectangle).  
Sans fonction, tu devrais répéter le même code plusieurs fois :  

```python
longueur = 10
largeur = 5
perimetre1 = 2 * (longueur + largeur)

longueur = 7
largeur = 3
perimetre2 = 2 * (longueur + largeur)
```
C’est répétitif, et si tu veux changer la formule, tu dois la modifier partout.

Avec une fonction, tu peux **regrouper** le code dans un bloc réutilisable :

```python
def perimetre_rectangle(longueur, largeur):
    return 2 * (longueur + largeur)

print(perimetre_rectangle(10, 5))
print(perimetre_rectangle(7, 3))
```

Les fonctions rendent le code :  
- plus **lisible**,  
- plus **court**,  
- plus **facile à corriger et à réutiliser**.

---

## 2. Définir une fonction

En Python, on définit une fonction avec le mot-clé `def`.

```python
def nom_de_la_fonction(param1, param2, ...):
    # bloc d'instructions
    return resultat
```

### Exemple simple

```python
def carre(x):
    return x * x
```

Appel de la fonction :
```python
print(carre(5))  # affiche 25
```

---

## 3. Paramètres et arguments

Les **paramètres** sont les variables définies entre les parenthèses dans la définition.  
Les **arguments** sont les valeurs passées lors de l’appel.

```python
def presentation(nom, age):
    print("Je m'appelle", nom, "et j'ai", age, "ans.")

presentation("Lina", 16)  # "Lina" et 16 sont les arguments
```

---

## 4. Fonctions avec ou sans valeur de retour

Certaines fonctions **renvoient** un résultat avec `return`, d’autres non.

### Avec `return`
```python
def somme(a, b):
    return a + b

x = somme(3, 4)
print(x)  # 7
```

### Sans `return`
```python
def afficher_bonjour():
    print("Bonjour !")

afficher_bonjour()
```

Une fonction sans `return` renvoie implicitement la valeur `None`.

---

## Exercices

### Exercice 1 : Compréhension
Écrire une fonction `salutation(nom)` qui affiche « Bonjour [nom] ! ».  
Appeler la fonction avec plusieurs prénoms.

---

### Exercice 2 : Calculs simples
Écrire une fonction `cercle(r)` qui renvoie le **périmètre** et l’**aire** d’un cercle de rayon `r`.

Rappel :  
- Périmètre = 2 × π × r  
- Aire = π × r²  

Utiliser `math.pi` (penser à importer le module `math`).

---

### Exercice 3 : Moyenne
Écrire une fonction `moyenne(a, b, c)` qui renvoie la moyenne de trois nombres.  
Tester la fonction avec différents ensembles de valeurs.

---

### Exercice 4 : Conversion
Écrire une fonction `celsius_vers_fahrenheit(temp)` qui renvoie la température convertie.  
Formule : `F = (9/5) * C + 32`.

---

### Exercice 5 : Mini-projet
Créer un programme complet qui :
1. Demande à l’utilisateur la longueur et la largeur d’un rectangle.  
2. Utilise une fonction pour calculer l’aire.  
3. Utilise une fonction pour calculer le périmètre.  
4. Affiche les résultats.

---

### Exercice 6 : Défi – Fonction imbriquée
Écrire une fonction `distance(x1, y1, x2, y2)` qui calcule la distance entre deux points du plan.  
Utiliser la fonction `racine_carree` que tu définiras toi-même.

Formule :  
\( d = \sqrt{(x2 - x1)^2 + (y2 - y1)^2} \)

---

## 7. Pour aller plus loin

Les fonctions sont la base de toute **programmation modulaire**.  
Elles permettent de :  
- clarifier les programmes,  
- éviter les répétitions,  
- faciliter les tests unitaires,  
- préparer l’introduction des **fonctions récursives** et de la **programmation orientée objet**.

