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