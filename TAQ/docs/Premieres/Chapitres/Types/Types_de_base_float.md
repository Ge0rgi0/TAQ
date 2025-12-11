# Types de base : flottants

Contrairement aux entiers, les **nombres réels** peuvent avoir une **partie fractionnaire**.  
Pour les représenter en informatique, on utilise le format **nombre à virgule flottante** (*floating point*).  

### Conversion décimal vers binaire

Prenons $6.34375_{10}$  
On peut séparer cette valeur en deux :  
- la partie entiére : 6  
- la partie fractionnaire : 0.34375  

On sait déja transformer les valeurs entiére : $6_{10} = 110_2$

Pour la partie fractionnaire, à l'inverse, on va effectuer des **multiplications successives** :
On multiplie notre valeur par 2. Puis on recommence avec la partie fractionnaire du resultat. Et ainsi de suite jusqu'à ce que le resultat soit une valeur entiére.

$0.34375 \times 2 = 0.6875$  
$0.6875 \times 2 = 1.375$  
$0.375 \times 2 = 0.75$  
$0.75 \times 2 = 1.5$  
$0.5 \times 2 = 1$

Pour finir on regarde les valeurs entiéres des resultats de haut en bas.  
On a donc comme partie fractionnaire : $0.01011_2$.

Pour finir, il nous suffit d'additionner nos deux résultats : $6.34375_{10} = 110.01011_2$.

---
### Conversion binaire vers décimal

Ici, nous utiliserons la même méthode que pour les valeurs entiéres.
Les bits de la partie fractionnaire correspondent à des puissances négatives.

Reprenons notre résultat précédent : $110.01011_2$.

|$2^2$|$2^1$|$2^0$|$2^{-1}$|$2^{-2}$|$2^{-3}$|$2^{-4}$|$2^{-5}$|
|-|-|-|-|-|-|-|-|
|1|1|0|0|1|0|1|1|

Pour retrouver notre valeur décimal nous pouvons effectuer ce calcul :  
$$
2^2 + 2^1 + 2^{-2}+ 2^{-4}+ 2^{-5} =
$$
$$4 + 2 + 0.25 + 0.0625 + 0.03125 = 6.34375
$$
---
*Rappel sur les puissances*

Une **puissance négative** permet de représenter la **division répétée**.  

- Pour tout nombre non nul \(a\) et tout entier \(n > 0\) :  
$$
a^{-n} = \frac{1}{a^n}
$$

Autrement dit, \(a^{-n}\) est l'inverse de \(a^n\).

| $2^-1$  | $2^-2$  | $2^-3$   | $2^-4$    | $2^-5$     | $2^-6$      | $2^-7$       |
|-------|-------|--------|---------|----------|-----------|------------|
| $\frac{1}{2^1}$| $\frac{1}{2^2}$|$\frac{1}{2^3}$| $\frac{1}{2^4}$| $\frac{1}{2^5}$| $\frac{1}{2^6}$| $\frac{1}{2^7}$|
| $\frac{1}{2}$| $\frac{1}{4}$| $\frac{1}{8}$| $\frac{1}{16}$| $\frac{1}{32}$| $\frac{1}{64}$| $\frac{1}{128}$|
| $0.5$   | $0.25$  | $0.125$  | $0.0625$  | $0.03125$  | $0.015625$  | $0.0078125$  |

<span style="color:blue">Exemples</span>

- \(2^{-3} = \frac{1}{2^3} = \frac{1}{8} = 0.125\)  
- \(5^{-2} = \frac{1}{5^2} = \frac{1}{25} = 0.04\)  
- \(10^{-4} = \frac{1}{10^4} = \frac{1}{10000} = 0.0001\)

---
### La norme IEEE 754

La norme **IEEE 754** définit comment représenter un réel sur un nombre fini de bits.  
Elle utilise trois composants :  

1. **Signe (1 bit)** : 0 → positif, 1 → négatif  
2. **Exposant** : encode la puissance de 2  
3. **Mantisse (ou fraction)** : encode les chiffres significatifs  

Le nombre réel est donc représenté comme :  

\[
x = (-1)^{\text{signe}} \times 1.\text{mantisse} \times 2^{\text{exposant}-\text{biais}}
\]

- Le **biais** est un nombre ajouté pour que l’exposant puisse être positif ou négatif.  
- La **mantisse** permet de représenter les chiffres significatifs.  

---

### Propriétés importantes

- Certains nombres ne peuvent pas être représentés exactement.  
  Exemple : \(0.1_{10}\) n’a pas de représentation binaire exacte.  
- Les erreurs d’arrondi peuvent s’accumuler lors des calculs.  
- Il ne faut **jamais tester l’égalité de deux flottants** avec `==`.  

<span style="color:blue">Exemples</span>  

- \(0.25_{10} = 0.01_2\) exactement  
- \(0.1_{10}\) = une suite infinie en binaire → approximation  
- \(1/3_{10} \approx 0.3333...\) → approximation  

<span style="color:red">Exercices</span>  

1. Convertir les nombres suivants en binaire flottant (approximatif sur 8 bits de mantisse) :  
   - 0.1  
   - 0.25  
   - 1/3  
2. Vérifier pourquoi `0.2 + 0.1 != 0.3` en Python ou en pseudo-code.  
