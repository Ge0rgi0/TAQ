# Algorithmes Gloutons

## Problème : le Rendu de Monnaie

Vous êtes caissier. Un client doit recevoir **48 centimes** de monnaie.  
Vous disposez de pièces de : **50c, 20c, 10c, 5c, 2c, 1c** (quantités illimitées).

**Questions :**

1. Quelle est la décomposition que vous feriez naturellement ? Combien de pièces utilisez-vous ?

2. Décrivez en français la **stratégie** que vous avez utilisée, étape par étape.

3. Pensez-vous que votre stratégie donne **toujours** le moins de pièces possible ? Pourquoi ?

---

La stratégie naturelle consiste à, à chaque étape, **prendre la plus grande pièce qui ne dépasse pas le montant restant**.

On appelle cette approche une **stratégie gloutonne** (*greedy* en anglais) : à chaque étape, on fait le choix localement optimal, sans revenir en arrière.

### Exercice 1 — Formalisons la stratégie

   | Étape | Montant restant | Pièce choisie | Montant restant après |
   |-------|----------------|---------------|-----------------------|
   | 1     | 63c            | ...           | ...                   |
   | 2     | ...            | ...           | ...                   |
   | ...   | ...            | ...           | ...                   |

1. Appliquez cette stratégie pour rendre **63 centimes**. Détaillez chaque étape dans le tableau.

2. Combien d'étapes a nécessité cet algorithme ? Est-ce prévisible ?

3. Que se passe-t-il si une pièce d'une certaine valeur est **absente** du système ? Essayez de rendre 30c sans pièce de 20c.

4. L'algorithme se termine-t'il toujours ? Pourquoi ? (Sans utiliser de variant)

---

### Exercice 2 — Coder l'algorithme glouton

Voici la spécification de la fonction à écrire :

```python
def rendu_monnaie(montant: int, pieces: list[int]) -> list[int]:
    """
    Calcule le rendu de monnaie par algorithme glouton.

    Stratégie : à chaque étape, on choisit la pièce de plus grande valeur
    qui ne dépasse pas le montant restant à rendre.

    Préconditions :
        - montant >= 0 (entier en centimes)
        - pieces est une liste d'entiers strictement positifs,
          triée par ordre décroissant
        - 1 doit figurer dans pieces pour garantir la terminaison

    Postconditions :
        - La somme des éléments de la liste retournée est égale à montant
        - La liste retournée contient uniquement des valeurs présentes dans pieces

    Paramètres :
        montant (int) : somme à rendre en centimes
        pieces  (list[int]) : valeurs des pièces disponibles, ordre décroissant

    Retourne :
        list[int] : liste des pièces utilisées (avec répétitions possibles)

    Exemples :
        >>> rendu_monnaie(41, [50, 20, 10, 5, 2, 1])
        [20, 20, 1]
        >>> rendu_monnaie(0, [50, 20, 10, 5, 2, 1])
        []
        >>> rendu_monnaie(6, [4, 3, 1])
        [4, 1, 1]
    """
    # À compléter
    ...
```

**Travail demandé :**

1. Complétez la fonction `rendu_monnaie`.

2. Testez-la avec les exemples de la docstring. Les résultats sont-ils ceux attendus ?

3. Proposer un invariant de boucle pour ce programme.

4. La fonction se termine-t'elle toujours ? Pourquoi ? (Avec un variant cette fois)

---

### Exercice 3 — Analyser la complexité

La **complexité temporelle** mesure le nombre d'opérations en fonction de la taille de l'entrée.

**Questions :**

1. Dans le pire cas (montant = N, uniquement des pièces de 1c), combien d'itérations effectue la boucle principale ?

2. Donnez la complexité en notation O(...) en fonction de `montant` et de `len(pieces)`.

3. Pour un montant de 10 000€ (1 000 000 centimes), estimez le nombre d'itérations dans le pire cas. Est-ce raisonnable ?
   > *Un ordinateur moderne effectue ~100 millions d'opérations par seconde.*

---

### Exercice 4 - Optimal ?

Reprenez le résultat du dernier test de votre fonction Python :

```python
rendu_monnaie(6, [4, 3, 1])
```

**Questions :**

1. Quelle réponse a donné votre algorithme ? Combien de pièces ?

2. Trouvez **à la main** une meilleure décomposition de 6 avec les pièces {4, 3, 1}.

3. L'algorithme glouton a-t-il trouvé la solution optimale ? Expliquez pourquoi il échoue ici.

4. Testez aussi `rendu_monnaie(30, [25, 10, 1])` et `rendu_monnaie(12, [10, 6, 1])`.  
   Dans chaque cas, trouvez la solution optimale à la main et comparez.

---

### Conclusion

**Questions :**

1. Quels sont les **avantages** des algorithmes gloutons ?

2. Quels sont leurs **inconvénients** ?

3. Comment pourrait-on résoudre le problème du rendu de monnaie de façon **toujours optimale** ?  
   *(Piste : imaginez tester toutes les combinaisons possibles… mais est-ce raisonnable ?)*

---

## Pour les élèves qui terminent tôt

### Défi 1 — Glouton optimal : preuve empirique

Écrivez une fonction `tester_optimalite(pieces: list[int], montant_max: int) -> bool` qui :
- teste le glouton pour **tous** les montants de 1 à `montant_max`
- pour chaque montant, compare le résultat du glouton avec une recherche exhaustive (force brute)
- retourne `True` si le glouton est optimal sur tous ces montants, `False` sinon

Testez-la sur le système euro et sur {1, 3, 4}.

---

### Défi 2 — Rendu de monnaie par force brute

Implémentez une fonction `rendu_optimal(montant: int, pieces: list[int]) -> list[int]` qui trouve la solution avec le **moins de pièces possible**, en explorant toutes les combinaisons (récursivité ou boucles imbriquées).

- Spécifiez les types et écrivez la docstring complète.
- Analysez sa complexité. Pourquoi est-elle beaucoup plus élevée que le glouton ?
- À partir de quel montant devient-elle inutilisable en pratique ?

---

### Défi 3 — Visualisation

Écrivez un programme qui affiche, pour un montant donné et un système de pièces donné, un **tableau comparatif** :

Montant : 6c 
Pièces : [4, 3, 1]

| Algorithme| Pièces  | Optimal ?|
|-----------|---------|----------|
| Glouton   | [4,1,1] |   NON    |
| Optimal   | [3,3]   |   OUI    |
