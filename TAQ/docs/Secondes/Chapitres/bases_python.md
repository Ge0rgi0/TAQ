# Cours : Bases de Python – Print, Variables et Input

**Objectifs :**
- Comprendre et utiliser `print` pour afficher des informations.
- Créer et manipuler des variables.
- Utiliser `input` pour récupérer des données de l’utilisateur.

---

## 2. Affichage avec `print`
**Théorie :**
- Syntaxe : `print("texte")`

**Exemples :**
```python
print("Bonjour Python !")
```

**Exercice rapide :**
- Afficher votre nom et votre âge.

---

## 3. Variables
**Théorie :**
- Définition d’une variable : "un nom qui contient une valeur".
- Affectation : `nom_variable = valeur`
- Types de variables : nombres (int, float), chaînes (str), booléens (bool)
- Conventions : noms clairs, pas d’espaces, sensible à la casse.

**Exemples :**
```python
nom = "Alice"
age = 17
print(nom, "a", age, "ans")
```

**Exercice pratique :**
- Créer deux variables : `prenom` et `ville`, puis les afficher dans une phrase.

---

## 4. Récupérer des données avec `input`
**Théorie :**
- Syntaxe : `variable = input("Question à l'utilisateur : ")`
- Les données reçues sont toujours de type `str`.
- Conversion de type si nécessaire : `int(input(...))` ou `float(input(...))`

**Exemples :**
```python
nom = input("Quel est ton nom ? ")
age = int(input("Quel est ton âge ? "))
print("Bonjour", nom, "tu as", age, "ans")
```

**Exercice pratique :**
- Demander à l’utilisateur son prénom et sa ville, puis afficher :
  `"Bonjour <prénom>, tu habites à <ville>."`
- Bonus : demander l’âge et afficher :
  `"L’an prochain, tu auras <âge+1> ans."`

---

## 5. Mise en pratique / mini-projet
- Combiner `print`, variables et `input` dans un petit script interactif.
- Exemple : un mini questionnaire ou calcul simple (ex : demander deux nombres et afficher leur somme).

---

## 6. Conclusion et récapitulatif
Points clés :
  - `print` = afficher
  - Variables = stocker des informations
  - `input` = récupérer des informations
