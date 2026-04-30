# Algorithmes Gloutons

## Problème — Rendre la monnaie

Un client paie son café 1,57 € avec un billet de 2 €.
Vous devez lui rendre **43 centimes**.  
Vous disposez de pièces de : **50c, 20c, 10c, 5c, 2c, 1c**.

**Sans réfléchir**, quelles pièces lui donneriez-vous ? Notez-les.

Comparez avec votre voisin. Avez-vous fait le même choix ? Utilisé le même nombre de pièces ?

Décrivez maintenant votre choix ainsi que la **règle** que vous avez appliquée, comme si vous l'expliquiez à quelqu'un qui ne l'a jamais fait.

---

La stratégie que vous avez décrite ressemble probablement à ceci : 
à chaque étape, **prendre la plus grande pièce qui ne dépasse pas le montant restant**, puis recommencer avec ce qui reste.

C'est une idée simple, mais elle a un nom en informatique : on appelle ça une **stratégie gloutonne** (*greedy* en anglais).
Le mot est imagé : l'algorithme est "gourmand", il veut toujours le maximum immédiatement, sans se préoccuper de la suite.

Plus formellement : à chaque étape, on dit que l'on fait le **choix localement optimal**, sans jamais revenir en arrière. On ne remet jamais en question une décision prise.

### Exercice 1 — Formalisons la stratégie

**1.** Appliquez la stratégie gloutonne pour rendre les montants suivants :

- 63c
- 1€28

Détaillez chaque étape dans un tableau :

| Étape | Pièce choisie | Montant restant |
|-------|----------------|---------------|
| 1     |                |               |                       
| 2     |                |               |                       
| ...   |                |               |                       

**2.** Comptez le nombre d'étapes pour chaque montant.
Pouvez-vous prévoir ce nombre **avant** d'appliquer l'algorithme ? De quoi dépend-il ?

**3.** Que se passe-t-il si une pièce est absente ?
Essayez de rendre 30c **sans utiliser la pièce de 20c**. Que remarquez-vous ?

**4.** L'algorithme se termine-t-il toujours ?
Justifiez en observant ce qui arrive au montant restant à chaque étape.
*(On ne demande pas de variant, une explication en français suffit.)*

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

2. Testez-la avec les exemples de la docstring.

3. Proposer un invariant de boucle pour ce programme.

4. La fonction se termine-t'elle toujours ? Pourquoi ?
*(Avec un variant cette fois)*

---

### Exercice 3 — Analyser la complexité

Rappel : La **complexité temporelle** mesure le nombre d'opérations en fonction de la taille de l'entrée.

1) Considérons le `montant = N`. Quel est le pire cas ? Dans cette situation :

>Combien de fois la boucle principale s'exécute-t-elle ?  
>Combien de pièces sont testées à chaque itération ?

2) En déduire la complexité en notation O(...) en fonction de `montant` et `len(pieces)`.
*(Aide : les deux paramètres n'ont pas le même rôle — lequel domine ?)*

3) Pour un montant de 10 000 €, estimez le nombre d'itérations dans le pire cas.
Est-ce raisonnable pour un ordinateur ?
*(Un ordinateur moderne effectue ~100 millions d'opérations simples par seconde.)*


---

### Exercice 4 - Optimal ?

Reprenez le résultat du dernier test de votre fonction Python :

```python
rendu_monnaie(6, [4, 3, 1])
```

1. Quelle réponse a donné votre algorithme ? Combien de pièces ?

2. Trouvez **à la main** une meilleure décomposition pour la valeur 6 avec les pièces {4, 3, 1}.

3. L'algorithme glouton a-t-il trouvé la solution optimale ? Expliquez pourquoi il échoue ici.

4. Testez aussi `rendu_monnaie(30, [25, 10, 1])` et `rendu_monnaie(12, [10, 6, 1])`.  
   Dans chaque cas, trouvez la solution optimale à la main et comparez.

---

### Conclusion

**Questions :**

1. Quels sont les **avantages** des algorithmes gloutons ?

2. Quels sont leurs **inconvénients** ?

3. Comment pourrait-on résoudre le problème du rendu de monnaie de façon **toujours optimale** ? Comparons l'efficacité de cette stratègie avec l'approche gloutonne.