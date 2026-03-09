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
- Clé : CLE ( c'est à dire les décalages successifs : 2, 11, 4)

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

#### Le chiffrement parfait : One-Time Pad

Un chiffrement symétrique est **théoriquement inviolable** uniquement si toutes les conditions suivantes sont réunies :

- la clé a **exactement la même longueur que le message** (résiste aux analyses statistiques)
- la clé est **totalement aléatoire**
- la clé n'est utilisée **qu'une seule fois**
- la clé reste **strictement secrète**

Ce type de chiffrement est appelé **chiffrement de Vernam** ou **One-Time Pad**.  
Dans ce cas, il est impossible, même avec une puissance de calcul infinie, de distinguer le message chiffré d'un message aléatoire.

Cependant c'est très couteux de l'appliquer ainsi aujourd'hui, surtout avec des transmissions aussi grandes.

#### Pourquoi les chiffrements symétriques classiques restent utilisés

Dans la pratique, ces conditions idéales ne sont jamais réunies :

- la clé est beaucoup plus courte que le message
- la clé est réutilisée
- le chiffrement produit des motifs exploitables statistiquement

Cela signifie que ces chiffrements ne sont pas parfaitement sûrs **en théorie**, mais qu'ils restent **très efficaces en pratique**.  
Des algorithmes modernes comme **AES** utilisent des clés courtes (128, 192 ou 256 bits) mais sont considérés comme sûrs car leur attaque nécessiterait un temps de calcul irréaliste.

<iframe width="400" height="300"
        src="https://www.youtube.com/embed/5ZEYKk8BHcE?start=65"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
</iframe>

    

#### Le problème de l'échange de clé

Le chiffrement symétrique repose sur une clé unique, utilisée à la fois pour chiffrer et déchiffrer le message.
Les deux personnes doivent donc posséder la même clé.

> **Le paradoxe de l'échange de clé :**  
> Pour communiquer de façon sécurisée, il faut d'abord partager une clé.  
> Mais partager cette clé nécessite déjà un canal sécurisé... qu'on n'a pas encore.

Si un attaquant intercepte la clé, **tous les messages passés et futurs sont compromis**.

**La solution : combiner les deux chiffrements**

Le problème de l'échange de clé est précisément ce que résout le **chiffrement asymétrique**.  
L'idée : utiliser RSA **uniquement pour transmettre la clé symétrique**, puis basculer sur AES pour la communication.

1. Bob génère une paire de clés **(publique / privée)**
2. Bob envoie sa **clé publique** à Alice — sans risque, elle peut être interceptée
3. Alice génère une **clé symétrique** (ex : clé AES)
4. Alice **chiffre cette clé AES** avec la clé publique de Bob
5. Bob **déchiffre** avec sa clé privée → il obtient la clé AES
6. Alice et Bob communiquent ensuite en **chiffrement symétrique**
```
Alice                          Bob
  |                             |
  |   ←——— clé publique ——————— |   (étape 2, non secrète)
  |                             |
  |   ——— clé AES chiffrée ———→ |   (étape 4, illisible sans clé privée)
  |                             |
  |   ←———— AES ————————————→   |   (étape 6, communication rapide)
```

> Eve peut intercepter la clé publique et la clé AES chiffrée,  
> mais **sans la clé privée de Bob, elle ne peut pas retrouver la clé AES**.

Cette combinaison donne le **meilleur des deux mondes** :

| | Symétrique (AES) | Asymétrique (RSA) |
|---|---|---|
| Vitesse | ✅ Rapide | ❌ Lent |
| Échange de clé | ❌ Problématique | ✅ Sécurisé |
| Rôle | Chiffrer les données | Transmettre la clé AES |

C'est exactement le fonctionnement de **HTTPS**, le protocole qui sécurise le Web.

---

## 2. Chiffrement asymétrique

### 2.1 Définition et principe

Le chiffrement asymétrique repose sur une paire de clés mathématiquement liées :

- une **clé publique** : diffusée librement, utilisée pour chiffrer
- une **clé privée** : gardée secrète, utilisée pour déchiffrer

> Ce qui est chiffré avec la clé publique ne peut être déchiffré qu'avec la clé privée correspondante.

Contrairement au chiffrement symétrique, il n'est plus nécessaire de partager une clé secrète au préalable. Cela résout le problème fondamental de l'échange de clés sur un canal non sécurisé.

### 2.2 Chiffrement RSA

RSA (du nom de ses inventeurs Rivest, Shamir et Adleman en 1977) est l'algorithme asymétrique le plus célèbre.
Sa sécurité repose sur un problème mathématique simple à poser mais extrêmement difficile à résoudre : la **factorisation de grands nombres entiers**.

> Multiplier deux grands nombres premiers est facile.
Retrouver ces deux facteurs à partir du produit est, en pratique, impossible en un temps raisonnable.

#### Fonctionnement

**1ère étape :** Choisir deux nombres premiers

On choisit deux nombres premiers ``p`` et ``q``, distincts et gardés secrets, puis on calcule leur produit :

> $n = p \times q$

``n`` est rendu publique (il fera partie de la clé), alors que ``p`` et ``q`` sont secrets.

> En pratique, on préférera que n soit très très grand.

**2ème étape :** calculer l'indicatrice d'Euler

On calcule : $φ(n) = (p - 1) \times (q - 1)$

Cette valeur est ``secrète`` et sert à construire les clés.

**3ème étape :** choisir l'exposant public ``e``

On choisit un entier ``e`` tel que :

- $1 < e < φ(n)$
- ``e`` et ``φ(n)`` sont premiers entre eux (leur PGCD vaut 1)

`e` fait partie de la clé ``publique``.

**4ème étape :**  Calculer l'exposant privé ``d``

On calcule d, l'inverse modulaire de e modulo ``φ(n)`` :

$d \times e ≡ 1 \mod φ(n)$

``d`` c'est la clé ``privée`` ! 

Le calculer sans connaître ``φ(n)`` (et donc sans connaître ``p`` et ``q``) est un problème très difficile (quasi impossible dans un temps raisonnable).

**Résumé de clés**

- publique : ( e , n )  
- privée : ( d , n )

**Pour chiffrer** un message ``M`` (représenté par un entier, avec ``M < n``) :

- $C = M^e \mod n$

**Pour déchiffrer** le message `C` :

- $M = C^d \mod n$

#### Exemple

**Objectif :** Alice veut envoyer le message ``M = 7`` à Bob de façon sécurisée.

**Étape 1 – Bob choisit ``p`` et ``q``**

- $p = 3$
- $q = 11$
- $n = p \times q = 33$

**Étape 2 – Bob calcule ``φ(n``)**

$φ(n) = (p − 1) \times (q − 1) = 20$  

**Étape 3 – Bob choisit ``e``**

On cherche ``e`` tel que ``PGCD(e, 20) = 1`` :

par exemple :  $e = 3$  

$PGCD(3, 20) = 1$ donc c'est bon !

>>>Clé publique de Bob : ``(e=3, n=33)``

**Étape 4 – Bob calcule ``d``**

On cherche ``d`` tel que $3\times d ≡ 1 \mod 20$ :

par exemple : $d = 7$  
$3 \times 7 = 21 ≡ 1 \mod 20$

>>>Clé privée de Bob : ``(d=7, n=33)``

**Étape 5 – Alice chiffre le message**

Alice utilise la clé publique de Bob ``(e=3, n=33)`` pour chiffrer ``M=7`` :

$C = M^e \mod n$  
>$= 7^3 \mod 33$  
>$= 343 \mod 33$  
>$= 13$  

Alice envoie ``C = 13`` à Bob.

**Étape 6 – Bob déchiffre**

Bob utilise sa clé privée ``(d=7, n=33)`` :

$M = C^d \mod n$  
>$= 13^7 \mod 33$  
>$= 62 748 517 \mod 33$  
>$= 7$  

Bob retrouve bien le message original.

### Activité – Chiffrement RSA en binôme

Vous allez jouer le rôle d'**Alice** et **Bob** (et éventuellement **Eve**) pour échanger un vrai message chiffré en RSA.

**Étape 1 – Bob génère ses clés**

Choisir deux nombres premiers `p` et `q`, puis compléter :

| | Valeur |
|---|---|
| `p` = | |
| `q` = | |
| `n = p × q` = | |
| `φ(n) = (p-1) × (q-1)` = | |

Choisir `e` tel que `1 < e < φ(n)` et `PGCD(e, φ(n)) = 1`.  
Calculer le PGCD à la main :
```
PGCD( ___ , ___ ) :
```

Calculer `d` avec : [https://www.dcode.fr/inverse-modulaire](https://www.dcode.fr/inverse-modulaire)  
$d \times e ≡ 1 \mod φ(n)$ 

| Clé publique | Clé privée |
|---|---|
| `(e = __ , n = __)` | `(d = __ , n = __)` |

**Étape 2 – Alice chiffre un message**

Choisir `M` un entier tel que `M < n`, puis chiffrer avec la clé publique de Bob :

$C = M^e \mod n$

**Étape 3 – Bob déchiffre**

$M = C^d \mod n$

### 2.3 Pourquoi RSA est sûr

La sécurité de RSA repose sur l'asymétrie entre deux opérations :

|Opération|Difficulté|
|--|--|
|Calculer ``n = p × q``|Facile (quelques microsecondes)|
|Retrouver ``p`` et ``q`` à partir de ``n``|Extrêmement difficile (années de calcul pour 2048 bits)|

Sans ``p`` et ``q``, il est impossible de calculer ``φ(n)``, donc impossible de trouver d à partir de ``e`` et ``n`` seuls.

**Avantages :** 

- Pas besoin de partager une clé secrète à l'avance  
- Permet l'authentification (signature numérique)

**Inconvénients :**  

- Beaucoup plus lent que le chiffrement symétrique  
- Utilisé uniquement pour chiffrer de petites données (ex : une clé AES)

## 3. HTTPS – Sécuriser le Web

### 3.1 Le problème de l'authentification

Jusqu'ici, nous avons supposé qu'Alice connaît avec certitude la clé publique de Bob.  
Mais comment s'en assurer sur Internet ?

> **Attaque de l'homme du milieu (Man-in-the-Middle) :**  

>Eve intercepte la clé publique de Bob avant qu'elle n'arrive à Alice, et la remplace par sa propre clé publique. Alice chiffre alors son message avec la clé d'Eve sans le savoir. Eve déchiffre le message, peut le lire ou le modifier, puis le rechiffre avec la vraie clé de Bob et le transmet. Bob reçoit le message normalement — ni Alice ni Bob ne détectent l'intrusion.
```
Alice                    Eve                     Bob
  |                       |                       |
  |  ←— clé publique Eve  |  ←— clé publique Bob  |
  |                       |                       |
  |  —— message chiffré → |  —— re-chiffré ——————→|
  |       (pour Eve)      |                       |
```

> Alice croit parler à Bob, mais Eve lit tout.

Pour résoudre ce problème, il faut un **tiers de confiance** capable de certifier que la clé publique appartient bien à son propriétaire.

---

### 3.2 Les certificats numériques

Un **certificat numérique** est un document électronique qui associe :

- une **clé publique**
- à une **identité** (nom de domaine, organisation…)
- signé par une **autorité de certification (CA)** de confiance

> **Analogie :** C'est comme une carte d'identité délivrée par l'État.  
> Vous faites confiance à la carte non pas parce que vous connaissez la personne,  
> mais parce que vous faites confiance à l'État qui l'a délivrée.

Les autorités de certification (DigiCert, Let's Encrypt, GlobalSign…) sont des organismes dont les clés publiques sont **pré-installées dans votre navigateur**.

Quand vous visitez `wikipedia.org`, le serveur envoie son certificat.  
Votre navigateur vérifie que ce certificat a bien été signé par une CA de confiance.  
Si oui, la clé publique est authentique. Eve ne peut pas falsifier ce certificat sans accès à la clé privée de la CA.

---

### 3.3 Déroulé d'une connexion HTTPS

HTTPS = HTTP + **TLS** (Transport Layer Security), le protocole qui sécurise la communication.

Voici les étapes d'une connexion HTTPS simplifiée :

**1. Le client demande une connexion sécurisée**

Votre navigateur contacte le serveur et indique qu'il veut communiquer en HTTPS.

**2. Le serveur envoie son certificat**

Le serveur transmet son certificat, qui contient sa **clé publique** et est signé par une CA.

**3. Le navigateur vérifie le certificat**

- La signature de la CA est-elle valide ?
- Le nom de domaine correspond-il ?
- Le certificat est-il encore valide (non expiré) ?

Si tout est bon, le cadenas s'affiche.

**4. Échange de clé symétrique**

Le navigateur génère une **clé de session** (clé AES aléatoire) et la chiffre avec la **clé publique du serveur**, et l'envoie.

**5. Le serveur déchiffre la clé de session**

Le serveur utilise sa **clé privée** pour obtenir la clé AES.  
Les deux parties possèdent maintenant la même clé symétrique.

**6. Communication chiffrée en AES**

Toute la suite de la communication est chiffrée en **AES**, rapide et sûr.
```
Navigateur                            Serveur
    |                                    |
    |  ——— "Je veux du HTTPS" ————————→  |
    |                                    |
    |  ←——— certificat (clé publique) —— |
    |                                    |
    |  [vérification du certificat]      |
    |                                    |
    |  ——— clé AES chiffrée (RSA) ——————→|
    |                                    |
    |  ←————— AES ————————————————————→  |
    |       (toute la communication)     |
```

---

### 3.4 Ce que garantit HTTPS

- **Confidentialité :** Chiffrement AES de toute la communication  
- **Intégrité :** Détection de toute modification des données  
- **Authentification :** Certificat signé par une autorité de confiance  

> HTTPS ne garantit **pas** que le site est honnête ou légitime.
> Il garantit uniquement que **vous communiquez bien avec ce site** et que **personne n'intercepte l'échange**. Un site de phishing peut très bien avoir un certificat HTTPS valide.
