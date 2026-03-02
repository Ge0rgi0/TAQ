# Sécurisation des communications

## Introduction

La sécurisation des communications vise à protéger les informations échangées entre deux entités (personnes, machines, serveurs) contre :

- l’écoute (confidentialité),
- la modification (intégrité),
- l’usurpation d’identité (authentification).

La cryptographie est l’outil principal permettant d’atteindre ces objectifs.  

**Définitions :**

- **Chiffrer :** consiste à transformer un message clair en un message illisible à l’aide d’un algorithme et d’une clé : ``Message clair → message chiffré``
- **Déchiffrer :** consiste à retrouver le message clair en connaissant la clé utilisée pour le chiffrement : ``Message chiffré + clé → message clair``
- **Décrypter :** Décrypter consiste à retrouver le message clair sans connaître la clé. ``C’est le travail du cryptanalyste.``

Dans le langage courant, **crypter** est souvent utilisé comme synonyme de chiffrer. Cependant, ce terme est impropre en cryptographie. ``On chiffre un message, on ne le “crypte” pas.``

On distingue principalement deux grandes familles de chiffrement :

- le **chiffrement symétrique**
- le **chiffrement asymétrique**

---

## 1. Chiffrement symétrique

Le chiffrement symétrique repose sur **une clé unique**, utilisée à la fois pour chiffrer et pour déchiffrer le message.  

### 1.1 Chiffrement de César

Le chiffrement de César est l’un des plus anciens algorithmes de chiffrement.

**Principe :**

- chaque lettre est décalée d’un nombre fixe de positions dans l’alphabet.

Exemple avec un décalage de 3 :

- A → D  
- B → E  
- Z → C  

Message clair : `BONJOUR`  
Message chiffré : `ERQMRXU`

**Avantages :**

- très simple à comprendre

**Inconvénients :**

- extrêmement faible
- facilement cassable par force brute

#### Exercices

Pour les exercices du chapitre, voici un fichier à compléter : [fichier python](sécurité_exo.py)

1. Chiffrer le mot `SECURITE` avec un décalage de 5.
2. Déchiffrer le message `CPGJID R THI BXTJM FJT DCT EXTRT` avec un décalage de 15.
3. Réaliser deux fonctions python, une pour chiffrer, l'autre pour déchiffrer, utilisant le chiffrement de César.
4. Réaliser une fonction permettant de déchiffrer un messange **sans connaître la clé**.

> On pourra utiliser les fonctions ``ord()`` et ``chr()``.  
> Rappel :  

> - ``ord(c : chr) -> int``, prend en paramètre un caractère et renvoie son code associé par la norme ISO.
> - ``chr(n : int) -> chr``, prend en paramètre un entier et renvoie le caractère associé par la norme ISO.
> - Dans la norme ISO, les lettres majuscules sont encodées de 65 à 90 inclus.

---

### 1.2 Chiffrement de Vigenère

Le chiffrement de Vigenère est une amélioration du chiffrement de César.

**Principe :**

- on utilise un mot-clé
- chaque lettre du message est chiffrée avec un décalage dépendant de la lettre du mot-clé

Exemple :

- Message : BONJOUR
- Clé : CLE

Chaque lettre de la clé correspond à un décalage différent.

**Avantages :**

- plus résistant que César
- clé plus difficile à deviner

**Inconvénients :**

- vulnérable à certaines analyses statistiques si la clé est courte

#### Exercices
1. Chiffrer `MESSAGE` avec la clé `CLE`.
2. Dechiffrer `EE ZDAAES IAUIPIKE IZQLBCUROT WQ GEBNWQS EFSIANFBBBXIGFS` avec la clè `BATMAN`.
3. Réaliser deux fonctions python, une pour chiffrer, l'autre pour déchiffrer, utilisant le chiffrement de Vigenère.

> Si la clé est `A,B`, les décalages seront `1,2`.  
> Pour retrouver les message originial il faudrait appliquer les décalages `-1,-2`.

---

### 1.3 Le chiffrement par XOR 

Il repose sur une opération logique binaire du même nom.

Principe :

- chaque caractère du message est converti en code numérique
- ce code est combiné avec une clé à l’aide de l’opérateur XOR
- l’opération XOR possède une propriété fondamentale : chiffrer et déchiffrer utilisent la même opération

*Exemple :*

- message = "BONJOUR"
- clé = "HI"

- B -> 66 -> 1000010
- H -> 72 -> 1001000

|  |  |1 |0 |0 | 0| 0| 1|0 |
|--|--|--|--|--|--|--|--|--|
|XOR| |1 |0 |0 | 1| 0| 0|0 |
|Résultat||0|0|0| 1| 0| 1|0 |

- 0001010 -> 10

|Caractère du message|Unicode|Caractère de la clé|Unicode|XOR|
|--|--|--|--|--|
|B |66|H |72|10|
|O |79|I |73|6|
|N |78|H |72|6|
|J |74|I |73|3|
|O |79|H |72|7|
|U |85|I |73|28|
|R |82|H |72|26|

>> message code : `10 6 6 3 7 28 26`

#### Exercice

Coder en python une fonction pour chiffrer un message en utilisant cette méthode.
>> L'opération `XOR` en Python s'écrit avec le symbole `^`. 

### 1.4 Pourquoi le chiffrement symétrique est problématique

#### Sécurité

Le chiffrement symétrique repose sur une clé unique, utilisée à la fois pour chiffrer et déchiffrer le message.
>> Les deux personnes doivent donc posséder la même clé.

Pour communiquer de manière sécurisée :

- il faut transmettre la clé
- mais transmettre la clé nécessite déjà un canal sécurisé

>> Si un attaquant intercepte la clé, tous les messages passés et futurs sont compromis

#### Taille de la clé

Un chiffrement symétrique est **théoriquement inviolable** uniquement si toutes les conditions suivantes sont réunies :

- la clé a **exactement la même longueur que le message** (resiste aux analyses statistiques)
- la clé est **totalement aléatoire**
- la clé n’est utilisée **qu’une seule fois**
- la clé reste **strictement secrète**

Ce type de chiffrement est appelé **chiffrement de Vernam** ou **One-Time Pad**.

Dans ce cas, il est impossible, même avec une puissance de calcul infinie, de distinguer le message chiffré d’un message aléatoire.

#### Pourquoi les chiffrements symétriques classiques restent utilisés

Dans la pratique :

- la clé est beaucoup plus courte que le message
- la clé est réutilisée
- le chiffrement produit des motifs exploitables statistiquement

Cela signifie que ces chiffrements ne sont pas parfaitement sûrs **en théorie**, mais qu’ils restent **très efficaces en pratique**.

Par exemple, des algorithmes modernes comme AES utilisent des clés courtes (128, 192 ou 256 bits) mais sont considérés comme sûrs car leur attaque nécessiterait un temps de calcul irréaliste.

<iframe width="400" height="300"
        src="https://www.youtube.com/embed/5ZEYKk8BHcE?start=65"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
</iframe>

---

## 2. Chiffrement asymétrique

Le chiffrement asymétrique repose sur **une paire de clés** :
- une clé publique (diffusée)
- une clé privée (secrète)

### 2.1 RSA

RSA est l’un des algorithmes asymétriques les plus connus.

**Principe simplifié :**
- la clé publique sert à chiffrer
- la clé privée sert à déchiffrer
- la sécurité repose sur la difficulté de factoriser de grands nombres premiers

**Avantages :**
- permet l’échange sécurisé de clés
- pas besoin de partager une clé secrète à l’avance

**Inconvénients :**
- plus lent que le chiffrement symétrique
- utilisé surtout pour chiffrer de petites données (ex : clés)

#### Exercice papier – RSA
1. Pourquoi RSA utilise-t-il de très grands nombres premiers ?
2. Quelle est la différence fondamentale entre clé publique et clé privée ?

---

## 3. HTTPS et sécurisation du Web

HTTPS est la version sécurisée de HTTP.

Lorsqu’un navigateur se connecte à un site HTTPS :
1. le serveur envoie son **certificat** (clé publique)
2. le navigateur vérifie l’authenticité du certificat
3. une clé symétrique est échangée grâce au chiffrement asymétrique
4. la communication se poursuit en **chiffrement symétrique**

👉 HTTPS combine donc :
- le chiffrement asymétrique (RSA, ECDHE…)
- le chiffrement symétrique (AES)

Objectifs :
- confidentialité des données
- intégrité des échanges
- authentification du serveur

---

## 4. Exercices de programmation (Python)

L’objectif est de produire un programme capable de **chiffrer et déchiffrer** des messages avec différentes stratégies.

### 4.1 César en Python

```python
def chiffre_cesar(message, decalage):
    resultat = ""
    for c in message:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultat += chr((ord(c) - base + decalage) % 26 + base)
        else:
            resultat += c
    return resultat

def dechiffre_cesar(message, decalage):
    return chiffre_cesar(message, -decalage)
```

Exercice :

adapter le programme pour accepter une clé saisie par l’utilisateur

---

### 4.2 Vigenère en Python

```python

def chiffre_vigenere(message, cle):
    resultat = ""
    cle = cle.lower()
    j = 0

    for c in message:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            decalage = ord(cle[j % len(cle)]) - ord('a')
            resultat += chr((ord(c) - base + decalage) % 26 + base)
            j += 1
        else:
            resultat += c
    return resultat

```

Exercice :

écrire la fonction de déchiffrement

gérer les caractères spéciaux

4.3 Mini-projet

Créer un programme qui :

propose le choix de l’algorithme (César, Vigenère, RSA simplifié)

chiffre ou déchiffre un message

affiche clairement les étapes

Bonus :

ajouter une interface texte

stocker les messages chiffrés dans un fichier

Conclusion

La sécurisation des communications repose sur :

des algorithmes mathématiquement robustes

une bonne gestion des clés

la combinaison intelligente de méthodes symétriques et asymétriques

Ces principes sont aujourd’hui au cœur d’Internet, des messageries et des systèmes informatiques modernes.