# Entiers et conditions

---

## 1. Les entiers (`int`) et les opérations

Jusqu’ici, nous avons utilisé uniquement des textes (*string*).  
Python permet aussi de manipuler des **nombres entiers** (*int*).  

On peut effectuer des opérations mathématiques :  

```python
a = 10
b = 3
print(a + b)   # addition
print(a - b)   # soustraction
print(a * b)   # multiplication
print(a // b)  # division entière
print(a % b)   # reste de la division (modulo)
```

Résultat :  
```
13
7
30
3
1
```

---

### Exercice 1  
1. Crée deux variables avec des valeurs entières.
2. Affiche :  
   - leur somme
   - leur différence

---

## 2. La fonction `int()`

La fonction **`input`** renvoie toujours un texte.  
Si l’on veut l’utiliser comme un nombre, il faut le convertir en entier avec **`int()`**.  

Exemple :  

```python
age = int(input("Quel est ton âge ? "))
print("Dans 5 ans, tu auras", age + 5, "ans.")
```

Ici, `int(input(...))` transforme la réponse en entier.  
On peut ensuite faire des calculs avec.  

---

### Exercice 2  
Demande à l'utilisateur les valeurs des deux variables `x` et `y`.
Affiche :
   - leur produit  
   - le reste de la division de `x` par `y`

---

## 3. Les conditions `if`, `elif`, `else`

En Python, on peut exécuter des instructions différentes selon une condition.  
On utilise **`if`**, éventuellement suivi de **`elif`** (sinon si), et enfin de **`else`** (sinon).  

Exemple :  

```python
age = int(input("Quel est ton âge ? "))

if age < 18:
    print("Tu es mineur.")
elif age == 18:
    print("Tu as exactement 18 ans.")
else:
    print("Tu es majeur.")
```

L’indentation est obligatoire après `if`, `elif`, `else`.  
Les conditions possibles : `<`, `<=`, `>`, `>=`, `==`, `!=`.  

---

### Exercice 3  
- Écris un programme qui demande un nombre à l’utilisateur :  
- si le nombre est positif, affiche `"Ce nombre est positif"`,  
- si le nombre est nul, affiche `"Ce nombre est nul"`,  
- sinon affiche `"Ce nombre est négatif"`.  

---

## 4. Série d’exercices

Écris un programme qui demande un âge et affiche :  
   - `"Tu es mineur"` si l’âge est strictement inférieur à 18,  
   - `"Tu es majeur"` sinon.  

Écris un programme qui demande deux nombres et affiche le plus grand des deux.  

Écris un programme qui demande un nombre et affiche :  
   - `"Pair"` si le nombre est divisible par 2,  
   - `"Impair"` sinon.  

Écris un programme qui demande une note sur 20 et affiche :  
   - `"Insuffisant"` si la note est strictement inférieure à 10,  
   - `"Assez bien"` si la note est entre 10 et 13,  
   - `"Bien"` si la note est entre 14 et 16,  
   - `"Très bien"` si la note est 17 ou plus.  

---

## 5. Exercices supplémentaires

Demande à l’utilisateur deux nombres et affiche leur moyenne.  

Demande un nombre à l’utilisateur et affiche :  
   - `"Multiple de 3"` si le nombre est divisible par 3,  
   - `"Pas multiple de 3"` sinon.  

Demande l’âge d’une personne et affiche :  
   - `"Enfant"` si l’âge est inférieur à 12,  
   - `"Adolescent"` si l’âge est entre 12 et 17 inclus,  
   - `"Adulte"` sinon.  

Demande à l’utilisateur un nombre entier et affiche :  
   - `"Divisible par 2 et par 3"` si c’est le cas,  
   - `"Pas divisible par 2 et 3 en même temps"` sinon.  

Demande trois notes sur 20, calcule la moyenne et affiche :  
   - `"Admis"` si la moyenne est supérieure ou égale à 10,  
   - `"Refusé"` sinon.  