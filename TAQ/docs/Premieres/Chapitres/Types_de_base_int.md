# Types de base : Entier

## Entier positif

### Le décimal

Depuis toujours, nous utilisons la base 10, sûrement parce que nous avons… 10 doigts.  
C'est ce que l'on appelle le système **décimal**, car nous utilisons 10 chiffres (de 0 à 9) pour représenter toutes les valeurs.  
Dans un nombre décimal, chaque position correspond à une puissance de 10, de droite à gauche.  

|     | $10^3$ | $10^2$ | $10^1$ | $10^0$ |
|-----|-------|-------|-------|-------|
|$2025_{10}$ | 2     | 0     | 2     | 5     |

$$
2025_{10} = 2 \times 10^3 + 0 \times 10^2 + 2 \times 10^1 + 5 \times 10^0
$$

$$
= 2 \times 1000 + 0 \times 100 + 2 \times 10 + 5 \times 1
$$
-------------------
*Rappel sur les puissances*

Une **puissance** est une façon d’écrire une multiplication répétée.  

- \( a^n \) se lit « a puissance n » et signifie que l’on multiplie \(a\) par lui-même \(n\) fois :  
$$
a^n = \underbrace{a \times a \times \dots \times a}_{n \text{ fois}}
$$

<span style="color:blue">exemples</span>  

- \( 2^3 = 2 \times 2 \times 2 = 8 \)  
- \( 5^0 = 1 \) (par convention, toute base non nulle à la puissance 0 vaut 1)  
- \( 10^4 = 10 \times 10 \times 10 \times 10 = 10000 \)

----------

### Le binaire

L’ordinateur utilise la base 2, appelée **binaire**, car les composants électroniques ne peuvent traiter que deux états :  
- **1** : présence d’une tension électrique  
- **0** : absence de tension électrique  

Il a donc fallu représenter toutes les informations en binaire. Dans ce système, il n’existe que deux symboles : 0 et 1, que l’on appelle des **bits** (contraction de binary digit).  

Chaque position dans un nombre binaire correspond à une **puissance de 2**, de droite à gauche.  

<span style="color:blue">exemple</span>

Prenons le nombre binaire : $1011_2$

On peut le décomposer en puissances de 2 :

|     | $2^3$ | $2^2$ | $2^1$ | $2^0$ |
|-----|-------|-------|-------|-------|
|$1011_2$ | 1     | 0     | 1     | 1     |

**Et le convertir en décimal** :

$$
1011_2 = 1 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 1 \times 2^0
$$

$$
= 2^3 + 2^1 + 2^0
$$

$$
= 8 + 2 + 1
$$

$$
= 11
$$

donc $1011_{2} = 11_{10}$

<span style="color:red">Exercice</span>  
Convertir en décimal, ces valeurs binaires :

- $110010_{2}$
- $1100100_{2}$
- $100100101_{2}$
-------
### Conversion du décimal vers le binaire

On utilise la **Méthode des divisions successives**

1. On **divise le nombre par 2**.  
2. On **note le reste** (0 ou 1).  
3. On recommence avec le **quotient**, jusqu’à obtenir 0.  
4. Le nombre binaire est obtenu en **lisant les restes de bas en haut**.

<span style="color:blue">exemple</span>

Représentons la valeur $50_{10}$ en binaire.

50 / 2 = 25 reste **0**  
25 / 2 = 12 reste **1**  
12 / 2 = 6 reste **0**  
6 / 2 = 3 reste **0**  
3 / 2 = 1 reste **1**  
1 / 2 = 0  reste **1**

donc $50_{10} = 110010_{2}$

<span style="color:red">Exercice</span>  
Convertir en binaire, ces valeurs décimales :

- $2025_{10}$
- $4050_{10}$
- $59400_{10}$

---
### L’hexadécimal

Un autre système de numération très utilisé en informatique est la **base 16**, appelée **hexadécimal**.  
Pourquoi ? Parce qu’il est plus **compact** que le binaire : au lieu de manipuler des suites très longues de 0 et 1, on peut les regrouper par 4 bits (4 chiffres binaires) et les écrire avec un seul chiffre hexadécimal.  

#### Les chiffres en base 16  

La base 16 utilise **16 symboles** différents :  
- de 0 à 9 (comme en décimal)  
- puis les lettres A, B, C, D, E, F pour représenter les valeurs 10 à 15.  

| Décimal | Hexadécimal |
|---------|-------------|
| 10      | A           |
| 11      | B           |
| 12      | C           |
| 13      | D           |
| 14      | E           |
| 15      | F           |

<span style="color:blue">exemple</span>

|     | \(16^1\) | \(16^0\) |
|-----|----------|----------|
| \(A2_{16}\) | A (= 10) | 2 |

\[
A2_{16} = 10 \times 16^1 + 2 \times 16^0
\]

\[
= 160 + 2
\]

\[
= 162_{10}
\]

---

#### Lien entre binaire et hexadécimal  

Chaque chiffre hexadécimal correspond à **4 bits** (car \(2^4 = 16\)).  


| Hexa    | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
|---------|------|------|------|------|------|------|------|------|
| Binaire | 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 |


| Hexa    | 8    | 9    | A    | B    | C    | D    | E    | F    |
|---------|------|------|------|------|------|------|------|------|
| Binaire | 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |

Cela permet de convertir facilement du **binaire en hexadécimal** en regroupant les bits par paquets de 4.  

<span style="color:blue">exemple</span>  

\(111011_{2}\)  

On regroupe par 4 bits (en partant de la droite) :  

|0011|1011|
|-|-|
|3|B|

Donc $111011_2 = 3B_{16}$

<span style="color:red">Exercice</span>  
Convertir en décimal :  

   - \(FF_{16}\)  
   - \(1A3_{16}\)  

Convertir en binaire :  

   - \(7C4_{16}\)
   - \(FADA_{16}\)

Convertir en hexadécimal :  

   - \(1999_{10}\)
   - \(59400_{10}\)
   - \(111100_{2}\)  
   - \(110100101111_{2}\)  
---------
## Entier relatif

Jusqu’ici, nous avons vu la représentation des **entiers positifs**.  
Mais il faut aussi représenter les **entiers relatifs** (positifs et négatifs).  

### Nombre de bits nécessaires

En binaire, la taille d’un entier est déterminée par le **nombre de bits** utilisés.  
Avec `n` bits, on peut représenter au maximum :  

\[
0 \; \leqslant \; N \; < \; 2^n
\]

Exemple :  
- avec **8 bits** (1 octet), on peut représenter 256 valeurs distinctes (de 0 à 255).  
- avec **16 bits**, on peut représenter 65 536 valeurs (de 0 à 65 535).   

**Les tailles courantes**

Les tailles les plus utilisées en informatique sont :  

- **8 bits** (1 octet)  
- **16 bits** (2 octets)  
- **32 bits** (4 octets)  
- **64 bits** (8 octets)  

Chaque taille limite l’intervalle de valeurs possibles.  

<span style="color:red">Questions</span>  
Combien de valeurs différentes peut-on représenter avec :  
1. 5 bits ?  
2. 10 bits ?  
3. 32 bits ? 

---

### Première idée : utiliser un bit de signe

Une première idée consiste à réserver le **bit de poids fort** (le plus à gauche) pour indiquer le signe : 
- 0 → nombre positif 
- 1 → nombre négatif 

On aurait alors les représentations suivantes sur 3 bits :  

| |négatif|positif|  
|-|-|-|  
|0|100|000|  
|1|101|001|  
|2|110|010|  
|3|111|011|  

**Problèmes de cette méthode** 

- **Deux représentations pour la valeur 0.**  
Cela introduit une incohérence et gaspille une combinaison binaire.  
  
- **Addition incorrecte**  
Exemple avec \( 5 + (-5) \) sur 8 bits:  
$00000101_2 + 10000101_2 = 10001010_2$  
C'est à dire $5 - 5 = - 10$, ce qui est évidemment faux !  

Il faut donc trouver une autre méthode.  

<span style="color:red">Exercice</span>  
- Donner les représentations binaires des valeurs entre -5 et 5 sur 4 bits.  
- Donner les représentations binaires des valeurs -67 sur 8 bits.

---

### Solution : le complément à 2

Pour corriger ces problèmes, on utilise la méthode du **complément à 2**.  

L’idée est comparable à un compteur :  
- Si on compte en arrière depuis **0**, on obtient directement le dernier nombre possible.  
- Exemple en base décimale avec deux chiffres : après `00`, si on soustrait 1, on tombe sur `99`, puis `98`, etc.  
De la même manière, en binaire, on utilise le "rebouclage" naturel des bits pour coder les nombres négatifs.  

| |négatif|positif|  
|-|-|-|  
|0|   |000|  
|1|111|001|  
|2|110|010|  
|3|101|011|  
|4|100|    |  

#### Méthode de construction

La méthode est simple :  
Pour représenter un nombre négatif, on écrit en binaire sa valeur absolue, on inverse ensuite tous les bits, puis on ajoute 1.

<span style="color:blue">Exemple</span>  

Imaginons que nous codions sur 4 bits.  
Nous voulons représenter la valeur -5.  

$5_{10} = 101_2$  
sur 4 bits : $0101_2$  
inversion des bits : $1010_2$  
+1 → $1011_2$  

Sur 4 bits, on répresente donc -5 comme ceci : $1011_2$.  

<span style="color:red">Exercice</span>  
Coder en complément à 2 sur 4 bits les valeurs entre -5 et 5 sur 4 bits.  

---

Cette fois-ci l'addition fonctionne :  

<span style="color:blue">Exemple</span>  

Essayons de nouveau \(5 + (-5)\) sur 8 bits,  
c'est à dire : $00000101_2 + 11111011_2$  

|retenue | 1| 1| 1| 1| 1| 1| 1| 1| 1|  |  
|-       |- |- |- |- |- |- |- |- |- |- |   
||||||||||||  
|        |  |0 |0 |0 |0 |0 |0 |1 |0 |1 |  
|**+**   |  |1 |1 |1 |1 |1 |1 |0 |1 |1 |  
||||||||||||  
|**=**   | 1|0 |0 |0 |0 |0 |0 |0 |0 |0 |  

On obtient alors : $100000000_2$, or nous sommes sur 8 bits donc on a bien :  
$5_{10} + (-5_{10}) = 00000101_2 + 11111011_2 = 00000000_2 = 0_{10}$  

<span style="color:red">Exercice</span>  
Vérifier à la main les additions suivantes en complément à 2 (sur 4 bits) :  
1. $2 + (-2)$  
2. $3 + (-1)$  
3. $-3 + (-2)$  

<span style="color:red">Exercice</span>  
Donner l’intervalle des entiers représentables avec :  
1. 8 bits non signés  
2. 8 bits avec bit de signe  
3. 8 bits en complément à 2  

Jusqu’ici, nous avons vu comment représenter et manipuler des nombres.  
En programmation, il est souvent nécessaire de **prendre des décisions** :  
exécuter certaines instructions seulement si une condition est vraie.  

En Python, cela se fait avec les mots-clés `if`, `elif` et `else`.

---