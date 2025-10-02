# Les chaînes de caractères (`str`)

## Définition
Une **chaîne de caractères** est une suite ordonnée de symboles (lettres, chiffres, ponctuation, espaces…).  
En Python, une chaîne est de type `str`.  
On peut l’écrire entre **guillemets simples** `'...'` ou **guillemets doubles** `"..."`.  
Si la chaînes est sur plusieurs lignes on utilisera trois guillemets simples.  

Exemples :
```python
mot = "Bonjour"
lettre = 'A'
phrase = "Ceci est une phrase."

multi-ligne = '''Ceci est  
  une chaîne de caractéres  
  très longue  
'''
```

---

## ASCII
ASCII signifie American Standard Code for Information Interchange
(en français : Code américain standard pour l’échange d’informations).  

C’est une norme de codage des caractères créée dans les années 1960.
Elle associe chaque symbole (lettre, chiffre, ponctuation, contrôle) à un nombre entier.  

- L’idée : comme l’ordinateur ne comprend que des nombres (en binaire), il faut une correspondance caractère ↔ nombre.  

![ASCII](ASCII.png)

<span style="color:blue">Exemple</span>  

Un texte encodé ressemeble donc à ce ceci :

"NSI" -> 4E 53 49 -> 01001110 01010011 01001001

<span style="color:red">Exercices</span> 

### Exercice 1 : Conversion binaire → texte
On te donne la suite binaire suivante (chaque octet correspond à un caractère ASCII) :

`0100100001100101011011000110110001101111`

1. Séparer chaque octet et convertis-le en décimal.  
2. Trouver le caractère ASCII correspondant à chaque nombre.  
3. Recomposer la chaîne de caractères.  

**Question** : Quelle est la chaîne finale ?

### Exercice 2 : Conversion hexadécimal → texte
On te donne la suite hexadécimale suivante :

`54 75 74 6F 72`


1. Convertis chaque code hexadécimal en décimal.  
2. Trouve le caractère ASCII correspondant.  
3. Recompose le mot complet.  

**Question** : Quel est le mot obtenu ?

## ISO-8859-1 et manipulation des caractères en Python

Après la norme ASCII, une extension appelée **ISO-8859-1** (ou Latin-1) a été créée pour représenter les caractères utilisés dans les langues européennes. Contrairement à ASCII qui utilise 7 bits (128 caractères), ISO-8859-1 utilise **8 bits** et peut coder **256 caractères**, incluant les lettres accentuées (é, à, ü, etc.), ainsi que certains symboles supplémentaires. Cette norme permet donc de gérer beaucoup plus de textes européens qu’ASCII.

En Python, on peut manipuler facilement les codes des caractères grâce aux fonctions intégrées :  

- `ord(caractère)` : retourne le code numérique du caractère (ASCII ou ISO-8859-1).  
```python  
  >>> ord('é') # str -> int (décimal)
  233
```
- `chr(code)` : retourne le caractère correspondant à un code numérique.


```python
>>> chr(233) # int (décimal) -> str
é
```

## Codage universel : UTF-8

Les normes comme ASCII et ISO-8859-1 permettent de coder respectivement l’anglais et les langues d’Europe de l’Ouest.  

Mais il ne s’agit là que d’une petite partie des besoins :  

- d’autres alphabets (grec, cyrillique, arabe, hébreu, chinois, japonais, coréen, etc.)  
- des symboles mathématiques,  
- des caractères techniques,  
- et, plus récemment, les émoticônes et emojis.  

Avec seulement 1 octet (256 possibilités), il est impossible de représenter tous ces caractères.

C’est pour répondre à ce problème qu’a été créée la norme Unicode, qui attribue à chaque caractère du monde un numéro unique (point de code).
Cependant, il fallait également définir un mode de représentation en mémoire de ces points de code.

À la fin des années 1990, un nouvel encodage s’impose progressivement : UTF-8.
Il sera adopté massivement au cours des années 2000, devenant le standard du web et des systèmes modernes.

UTF-8 s’appuie sur le point de code de chaque caractère.
Un point de code est un identifiant numérique unique défini par la norme Unicode, qui répertorie aujourd’hui près de 138 000 caractères.

Les 256 premiers points de code correspondent aux caractères de l’ISO-8859-1, assurant ainsi la compatibilité avec les alphabets occidentaux.
On note un point de code sous la forme U+xxxx, où xxxx est la valeur en hexadécimal.

<span style="color:blue">Exemples</span>

- U+00E0 correspond au caractère `à`
- U+0052 correspond au caractère `R`

### Conversion

Les 127 premiers caractères (0 à 127) sont codés sur un seul octet : UTF-8 est donc totalement compatible avec ASCII.

Les autres caractères nécessitent plusieurs octets (jusqu’à 4 octets).

**Règles d’encodage**

Cas ASCII (1 octet) :

- Si le bit de poids fort (le premier à gauche) vaut 0, l’octet correspond directement à un caractère ASCII (codé sur les 7 bits restants).

Caractères sur plusieurs octets :

- Si le bit de poids fort vaut 1, alors la séquence de bits initiaux indique le nombre total d’octets utilisés pour représenter le caractère.

Cette séquence se compose d’une série de 1 consécutifs suivis d’un 0.

<span style="color:blue">Exemples</span>

- 0xxxxxxx → le caractère est codé sur 1 octet
- 110xxxxx → encodage sur 2 octets
- 1110xxxx → encodage sur 3 octets
- 11110xxx → encodage sur 4 octets

Octets de continuation

Dans un encodage sur k octets, les k − 1 octets suivants (appelés octets de continuation) commencent toujours par 10.

Leur forme est donc 10xxxxxx.

|Nombre d'octets|Forme de la représentation binaire|Caractères (points de code|
|--|--|--|
|1|<span style="color:red">0</span><span style="color:blue">xxxxxxx</span>|U+0000 -> U+007F|
|2|<span style="color:red">110</span><span style="color:blue">xxxxx</span> <span style="color:red">10</span><span style="color:blue">xxxxxx</span>|U+0080 -> U+07FF|
|3|<span style="color:red">1110</span><span style="color:blue">xxxx</span> <span style="color:red">10</span><span style="color:blue">xxxxxx</span> <span style="color:red">10</span><span style="color:blue">xxxxxx</span>|U+0800 -> U+FFFF|
|4|<span style="color:red">11110</span><span style="color:blue">xxx</span> <span style="color:red">10</span><span style="color:blue">xxxxxx</span> <span style="color:red">10</span><span style="color:blue">xxxxxx</span> <span style="color:red">10</span><span style="color:blue">xxxxxx</span>|U+10000 -> U+10FFFF|

<span style="color:red">Exercices</span>

Vous aurez besoin des fonctions `ord()` et `chr()`.

Convertir les caractères suivants en UTF-8 (donner la valeur binaire puis hexadécimale) :  
- `A`  
- `z`  
- `0`  
- `?`  
- `é`  
- `ç`  
- `à`  


Donner la représentation UTF-8 (binaire puis hexadécimale) des caractères suivants :  
- `€` (U+20AC)  
- `Ω` (U+03A9)  
- `漢` (U+6F22)  

On vous donne des séquences UTF-8. Donner le caractère correspondant.  

- `01000001`  
- `11000011 10101001`  
- `11100010 10000010 10101101`  
- `11100110 10111101 10100000`  

---

## En python

### Concaténation (`+`)
```python
prenom = "Ada"
nom = "Lovelace"
print(prenom + " " + nom)  # Ada Lovelace
```

### Répétition (`*`)
```python
rire = "ha"
print(rire * 3)  # hahaha
```

### Longueur (`len`)
```python
texte = "Bonjour"
print(len(texte))  # 7
```

### Accès par indice
Chaque caractère est accessible par son **indice** (position, en commençant à 0) :
```python
mot = "Python"
print(mot[0])  # P
print(mot[3])  # h
```

### Tranches (slices)
On peut extraire une partie de la chaîne :
```python
mot = "Python"

print(mot[1:4])    # yth   (du 2e caractère inclus au 4e exclu)
print(mot[-2:])    # on    (les 2 derniers caractères)
print(mot[:-2])    # Pyth  (tout sauf les 2 derniers)
print(mot[::2])    # Pto   (un caractère sur deux)
print(mot[1::2])   # yhn   (un caractère sur deux en commençant à l’indice 1)
print(mot[::-1])   # nohtyP (toute la chaîne à l’envers)
print(mot[3:0:-1]) # hty   (du 4e caractère vers le 1er en sens inverse)
```

### Fonctions utiles

```python
texte = "bonjour"
print(texte.upper())   # BONJOUR
print(texte.capitalize())  # Bonjour
print(texte.isalpha()) # True si uniquement des lettres
print(texte.isdigit()) # True si uniquement des chiffres
print("123".isdigit()) # True
```

### Caractéres spéciaux

- `\n` : saut de ligne (newline)  
- `\t` : tabulation (tab)  
- `\\` : antislash  
- `\'` : apostrophe simple  
- `\"` : guillemet double

### Parcours

On peut parcourir les chaînes de caractéres grâce à une boucle `for`.

```python
a = "azerty"
for c in a:
  print(c)
```
affichera :

```
a
z
e
r
t
y
```

---

## Exercices

### Exercice 1
Demander un mot et afficher son premier et son dernier caractère.

### Exercice 2
Demander une phrase et afficher sa longueur.

### Exercice 3
Vérifier si une chaîne donnée contient uniquement des chiffres.

### Exercice 4
Écrire un programme qui inverse une chaîne de caractères (sans utiliser un pas négatif).

### Exercice 5
Écrire un programme qui compte le nombre de fois qu'un caractére précis apparait dans une chaîne de caractéres.

### Exercice 6
Demander un mot et afficher `"Palindrome"` s’il se lit dans les deux sens.

### Exercice 7
Écrire un programme qui affiche une chaine de caractére en plusieurs parties distinctes. Chaque partie commence après une virgule.

```Salut, ça va ?```

donne donc :

```
Salut
ca va ?
```

### Exercice 8
Le code de César est une méthode de chiffrement très simple utilisée par Jules César dans ses correspondances secrètes (ce qui explique le nom).  L'idée est simple, nous choisissons une clé qui correspond à un décalage que nous allons appliquer sur chacun des caractéres du message.  

Exemple :  

Message : NSI  
Clé : 1  
Message codé : OTJ  

Message : NSI  
Clé : 25  
Message codé : MRK  

Imaginer un programme qui demande un message et une clé et qui affiche le message codé correspondant.  
