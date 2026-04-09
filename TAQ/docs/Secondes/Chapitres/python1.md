# Les bases : `print`, variables, `input`
---

## 1. Afficher du texte avec `print`

En Python, la fonction `print` permet d'afficher du texte à l'écran.  
Il faut écrire le texte **entre guillemets** (`"` ou `'`) et l'entourer de **parenthèses**.

```python
print("Bonjour tout le monde !")
print('Python est un langage simple.')
```

**Résultat :**
```
Bonjour tout le monde !
Python est un langage simple.
```

Les **parenthèses** indiquent ce qu'on veut afficher.  
Les **guillemets** indiquent qu'il s'agit d'un texte (on appelle ça une *chaîne de caractères*, ou *string* en anglais).

On peut afficher plusieurs éléments sur la même ligne en les séparant par des virgules :

```python
print("Mon prenom est", "Alice", "et j'ai", 15, "ans.")
```

**Résultat :**
```
Mon prenom est Alice et j'ai 15 ans.
```

Python ajoute automatiquement un espace entre chaque élément séparé par une virgule.

---

### `end=""` : contrôler la fin d'un affichage

Par défaut, `print` passe toujours à la ligne suivante après avoir affiché le texte. On peut changer ce comportement avec le paramètre `end`.

```python
print("Bonjour")
print("tout le monde")
```

**Résultat :**
```
Bonjour
tout le monde
```

Avec `end=""`, on supprime ce retour à la ligne automatique :

```python
print("Bonjour", end="")
print("tout le monde")
```

**Résultat :**
```
Bonjourtout le monde
```

Les deux textes sont collés. On peut mettre ce qu'on veut entre les guillemets de `end` :

```python
print("Bonjour", end=" ")
print("tout le monde")
```

**Résultat :**
```
Bonjour tout le monde
```

```python
print("un", end=" - ")
print("deux", end=" - ")
print("trois")
```

**Résultat :**
```
un - deux - trois
```

`end=""` est utile quand on veut construire une ligne morceau par morceau, au lieu d'afficher chaque `print` sur sa propre ligne.

---

### Exercice 1

Écris un programme qui affiche sur **une seule ligne**, en utilisant plusieurs `print` avec `end` :

```
Lundi - Mardi - Mercredi
```

---

## 2. Les variables

Une **variable** permet de stocker une information et de la réutiliser plus tard dans le programme.  
On utilise le signe `=` pour donner une valeur à une variable.

```python
prenom = "Alice"
print(prenom)
```

**Résultat :**
```
Alice
```

La variable `prenom` contient le texte `"Alice"`. Quand on écrit `print(prenom)`, Python affiche la valeur stockée dedans — sans guillemets cette fois, car `prenom` est une variable, pas du texte brut.

On peut changer la valeur d'une variable à tout moment :

```python
prenom = "Alice"
print(prenom)
prenom = "Bob"
print(prenom)
```

**Résultat :**
```
Alice
Bob
```

La deuxième ligne `prenom = "Bob"` **écrase** la valeur précédente. La variable ne retient que la dernière valeur qui lui a été assignée.

On peut aussi stocker des nombres dans une variable :

```python
age = 15
print("J'ai", age, "ans.")
```

**Résultat :**
```
J'ai 15 ans.
```

Les nombres ne prennent pas de guillemets. `age = 15` stocke le nombre 15, alors que `age = "15"` stockerait le texte `"15"` — ce n'est pas la même chose pour Python.

---

### Exercice 2

1. Crée une variable `animal` contenant le texte `"chien"`.
2. Affiche son contenu avec `print`.
3. Change la valeur de `animal` en `"chat"` et affiche-la à nouveau.

---

## 3. Demander une valeur à l'utilisateur avec `input`

La fonction `input` permet de poser une question à l'utilisateur et de récupérer ce qu'il écrit au clavier.

```python
nom = input("Quel est ton nom ? ")
print("Bonjour", nom, "!")
```

**Exemple d'exécution :**
```
Quel est ton nom ? Alice
Bonjour Alice !
```

Le texte entre parenthèses de `input` est affiché comme une question.  
Ce que l'utilisateur tape est stocké dans une variable — ici `nom`.  
On peut ensuite l'utiliser comme n'importe quelle autre variable.

On peut combiner `input` et `end` pour afficher la question et la réponse sur la même ligne :

```python
prenom = input("Entre ton prenom : ")
print("Enchante, ", end="")
print(prenom, end="")
print(" !")
```

**Exemple d'exécution :**
```
Entre ton prenom : Alice
Enchante, Alice !
```

---

### Exercice 3

Écris un programme qui demande le prénom de l'utilisateur et affiche :

```
Enchante, <prenom> !
```

---

## 4. Exercices

### Exercice 1

Écris un programme qui :
- demande le prénom de l'utilisateur avec `input`
- stocke la réponse dans une variable `prenom`
- affiche : `Bonjour <prenom>, bienvenue dans ton premier programme Python !`

### Exercice 2

Écris un programme qui :
- demande à l'utilisateur le nom d'un animal
- stocke la réponse dans une variable `animal`
- affiche : `J'aimerais avoir un <animal>.`

### Exercice 3

Écris un programme qui :
- demande à l'utilisateur son film préféré
- stocke la réponse dans une variable `film`
- affiche sur une seule ligne en utilisant `end` : `Ton film prefere est <film>.`

### Exercice 4

Écris un programme qui demande le prénom et l'âge de l'utilisateur, puis affiche :

```
<prenom> a <age> ans.
```