# Cours 1 – Print, variables, input  

## 1. Afficher du texte avec `print`

En Python, la fonction **`print`** permet d’afficher du texte à l’écran.  
Il faut écrire le texte **entre guillemets** (`"` ou `'`) et mettre des **parenthèses**.  

Exemple :  

```python
print("Bonjour tout le monde !")
print('Python est un langage simple.')
```

Les **parenthèses** indiquent ce qu’on veut afficher.  
Les **guillemets** indiquent qu’il s’agit d’un texte (une chaîne de caractères, ou *string*).

### Exercice 1  
Écris un programme qui affiche une phrase vous présentant (prénom, âge, etc)...

---

## 2. Les variables

Une **variable** permet de stocker une information et de la réutiliser.  
On utilise le signe **`=`** pour donner une valeur à une variable.  

Exemple :  

```python
prenom = "Alice"
print(prenom)
```

Résultat :  
```
Alice
```

Ici, la variable `prenom` contient le texte `"Alice"`.  
Quand on écrit `print(prenom)`, Python affiche la valeur stockée.  

On peut aussi changer la valeur d’une variable :  

```python
prenom = "Alice"
prenom = "Bob"
print(prenom)
```

Résultat :  
```
Bob
```

### Exercice 2  
1. Crée une variable `animal` contenant le texte `"chien"`.  
2. Affiche son contenu avec `print`.  
3. Change la valeur de `animal` en `"chat"` et affiche-la à nouveau.  

---

## 3. Demander une valeur à l’utilisateur avec `input`

La fonction **`input`** permet de poser une question à l’utilisateur et de récupérer ce qu’il écrit.  

Exemple :  

```python
nom = input("Quel est ton nom ? ")
print("Bonjour ", nom, " !")
```

Le texte dans les parenthèses de `input` est affiché comme une question.  
Ce que l’utilisateur écrit est stocké dans une variable (ici `nom`).  
On peut ensuite l’afficher avec `print`.  

### Exercice 3  
Écris un programme qui :  
1. Demande ton prénom avec `input`.  
2. Affiche :  
```
Enchanté, <ton prénom> !
```

---

## 4. Exercices

### Exercice 1  
Écris un programme qui :  
1. Demande ton prénom avec `input`.  
2. Stocke la réponse dans une variable `prenom`.  
3. Affiche : Bonjour `prenom`, bienvenue dans ton premier programme Python !

### Exercice 2  
Écris un programme qui :  
1. Demande à l’utilisateur le nom d’un animal.  
2. Stocke la réponse dans une variable `animal`.  
3. Affiche une phrase du type :  J'aimerais avoir un `animal`.

### Exercice 3  
Écris un programme qui :  
1. Demande à l’utilisateur son film préféré.  
2. Stocke la réponse dans une variable `film`.  
3. Affiche :  Ton film préféré est `film`.