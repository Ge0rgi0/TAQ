# Programmation Dynamique

## Rappel — Là où le glouton a échoué

Dans le cours précédent, vous avez implémenté l'algorithme glouton pour le rendu de monnaie.
Il donnait de bons résultats avec le système européen, mais échouait sur certains systèmes de pièces.

Rappelez-vous :

```python
rendu_monnaie(6, [4, 3, 1])  # → [4, 1, 1]  (3 pièces)
```

Pourtant, **[3, 3]** suffit — seulement 2 pièces.

Le glouton a fait un mauvais choix en prenant 4, et il ne peut **jamais revenir en arrière**.
C'est précisément ce que la programmation dynamique va corriger.

---

## Le problème, reformulé

**Entrée :** un montant `n` (en centimes) et une liste de valeurs de pièces disponibles.

**Sortie :** le **nombre minimal** de pièces pour atteindre exactement `n`.

On va maintenant chercher à résoudre ce problème de façon **toujours optimale**.

---

## Idée centrale : décomposer en sous-problèmes

Posons la question autrement.

Pour rendre `n` centimes en un minimum de pièces, je peux choisir **n'importe quelle pièce `p`** comme dernière pièce utilisée. Il me reste alors à rendre `n - p` centimes, toujours de façon optimale.

Autrement dit :

> **Le meilleur rendu pour `n`** = 1 (la pièce choisie) + **le meilleur rendu pour `n - p`**

Et on choisit la pièce `p` qui minimise ce total.

Formellement, si on note `opt(n)` le nombre minimal de pièces pour rendre `n` :

```
opt(0) = 0
opt(n) = 1 + min{ opt(n - p)  |  p ∈ pieces,  p ≤ n }
```

Cette formule s'appelle une **relation de récurrence** (ou équation de Bellman).

### Exercice 0 — Comprendre la récurrence

Avec les pièces {4, 3, 1}, calculez **à la main** :

1. `opt(0)`, `opt(1)`, `opt(2)`, `opt(3)`, `opt(4)`
2. En utilisant ces résultats, calculez `opt(5)` et `opt(6)`.
3. Vérifiez que `opt(6) = 2` et identifiez quelle pièce a été choisie à chaque étape.

---

## Naïf mais correct : la récursion

La récurrence se traduit presque directement en Python :

```python
def opt_naif(n: int, pieces: list[int]) -> int:
    """
    Retourne le nombre minimal de pièces pour rendre n centimes.
    Approche récursive naïve (sans mémoïsation).

    Préconditions :
        - n >= 0
        - 1 doit figurer dans pieces (garantit qu'une solution existe)
        - pieces contient des entiers strictement positifs

    >>> opt_naif(6, [4, 3, 1])
    2
    >>> opt_naif(0, [4, 3, 1])
    0
    >>> opt_naif(11, [10, 6, 1])
    2
    """
    if ... :
        return ...
    return ...
```

### Exercice 1 — Tester et observer

1. Codez et testez `opt_naif` avec les exemples de la docstring.

2. Tracez à la main **l'arbre des appels récursifs** pour `opt_naif(6, [4, 3, 1])` :

>Combien d'appels sont effectués en tout ?  
>Certains calculs sont-ils répétés ? Lesquels ?  

3. Essayez `opt_naif(40, [25, 10, 1])`. Que remarquez-vous ?
   *(Attendez 10 secondes. Si rien ne s'affiche, interrompez avec Ctrl+C.)*

---

## Le problème : des calculs répétés

Vous avez sûrement observé que `opt_naif` recalcule les mêmes valeurs des dizaines, voire des milliers de fois.

Par exemple, pour `opt(6)` avec les pièces {4, 3, 1} :

- `opt(2)` est calculé depuis `opt(3)` (via la pièce 1), mais aussi depuis `opt(6)` (via la pièce 4, puis pièce 1, puis...).

C'est un problème de **sous-problèmes qui se chevauchent** (*overlapping subproblems*).

La solution : **mémoriser** chaque résultat dès qu'on le calcule, pour ne jamais le recalculer.
Cette technique s'appelle la **mémoïsation**.

---

## Mémoïsation : ne jamais calculer deux fois la même chose

```python
def opt_memo(n: int, pieces: list[int], memo: dict = None) -> int:
    """
    Retourne le nombre minimal de pièces pour rendre n centimes.
    Approche récursive avec mémoïsation.

    >>> opt_memo(6, [4, 3, 1])
    2
    >>> opt_memo(0, [4, 3, 1])
    0
    """
    if memo is None:
        ...
    if n == ... :
        ...
    if n not in memo :
        ...
    return ...
```

### Exercice 2 — Comparer naïf et mémoïsé

1. Complétez `opt_memo` et testez-la avec les mêmes exemples qu'avant.

2. Comparez le nombre d'appels pour `opt_naif(6, [4, 3, 1])` vs`opt_memo(6, [4, 3, 1])`.

3. Comparez le nombre d'appels effectués pour les valeurs `5`, `10`, `15` avec les méthodes naïve et mémoïsée.

4. Quelle relation observez-vous entre `n` et le nombre d'appels mémoïsés ?

---

## Approche ascendante : remplir un tableau

La mémoïsation part de `n` et descend vers 0. On peut aussi faire **l'inverse** : partir de 0 et monter jusqu'à `n`, en remplissant un tableau `dp` tel que `dp[i]` est le nombre minimal de pièces pour rendre `i` centimes.

C'est l'approche **tabulaire** (ou *bottom-up*), la forme la plus classique de programmation dynamique.

```python
def rendu_monnaie_dp(montant: int, pieces: list[int]) -> int:
    """
    Retourne le nombre minimal de pièces pour rendre `montant` centimes.
    Approche tabulaire (bottom-up).

    Préconditions :
        - montant >= 0
        - pieces contient des entiers strictement positifs
        - 1 doit figurer dans pieces

    Postconditions :
        - Retourne le nombre minimal de pièces

    >>> rendu_monnaie_dp(6, [4, 3, 1])
    2
    >>> rendu_monnaie_dp(0, [4, 3, 1])
    0
    >>> rendu_monnaie_dp(11, [10, 6, 1])
    2
    """
    memo = 
    memo[0] = ...
    
    for i in range(...):
        ...
        
    return ...
```

### Exercice 3 — Comprendre le tableau

1. Exécutez `rendu_monnaie_dp` pour `montant = 6` et `pieces = [4, 3, 1]`.
   Affichez le tableau `dp` complet après exécution.

2. Avec cette stratégie, combien de pièces sont nécessaires pour les valeurs allant de 0 à 6.

3. Proposez un **invariant de boucle** pour la boucle externe (`for i in range(...)`).

4. La fonction se termine-t-elle toujours ? Justifiez avec un **variant**.

---

### Exercice 4 — Analyser la complexité

1. Combien de cases le tableau `dp` contient-il ?

2. Pour chaque case, combien d'opérations effectue-t-on ?

3. En déduire la complexité en notation O(...) en fonction de `montant` et `len(pieces)`.

4. Comparez avec la complexité du glouton. Lequel est plus rapide ? Lequel donne toujours la solution optimale ?

5. Pour `montant = 10 000` et 6 pièces, estimez le nombre d'opérations. Est-ce raisonnable ?

---

### Exercice 5 *(pour les rapides)* — Retrouver les pièces utilisées

`rendu_monnaie_dp` retourne seulement le nombre de pièces.
Écrivez `rendu_monnaie_dp_complet` qui retourne la liste des pièces utilisées.

```python
def rendu_monnaie_dp_complet(n: int, pieces: list) -> list:
    """
    >>> rendu_monnaie_dp_complet(6, [4, 3, 1])
    [3, 3]
    >>> rendu_monnaie_dp_complet(0, [4, 3, 1])
    []
    """
    # À compléter
```

**Aides :**
- Au lieu de stocker un entier dans `memo[i]`, stockez directement la liste des pièces.
- `memo[0]` vaut quoi ?
- Pour chaque montant `i`, comment obtenir `memo[i]` à partir de `memo[i - piece]` ?

---

## Conclusion — Glouton vs Programmation Dynamique

**Questions :**

**Questions :**
 
1. Quels sont les **avantages** de la programmation dynamique par rapport au glouton ?

2. Quels sont ses **inconvénients** ?