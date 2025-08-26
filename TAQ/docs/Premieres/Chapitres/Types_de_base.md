# Types de base

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

*<span style="color:blue">exemple</span>*

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

Donc $110010_2 = 32_{16}$

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
