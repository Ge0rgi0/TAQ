# Arbres Binaires de Recherche

## Introduction

Supposons qu'on dispose d'une liste de 1 000 000 d'entiers et qu'on cherche à savoir si la valeur `42` en fait partie.

- Dans une **liste non triée**, on est obligé de parcourir tous les éléments un par un → **O(n)**
- Dans une **liste triée**, on peut utiliser la recherche dichotomique → **O(log n)**
    - Mais insérer dans une liste triée reste coûteux, puisqu'il faudrait décaler tous les éléments plus grands → **O(n)**

Il nous faudrait donc une structure qui permette à la fois une recherche et une insertion efficaces.

Pour cela, nous allons utiliser un type particulier d'**arbre binaire** : l'**arbre binaire de recherche (ABR)**.

![](ABR.png)

On remarque que pour **chaque nœud** :
- toutes les valeurs dans son sous-arbre **gauche** lui sont **inférieures**
- toutes les valeurs dans son sous-arbre **droit** lui sont **supérieures**.

**Exercices**

1) Donner tous les ABR formés de trois nœuds et contenant les entiers 1, 2 et 3.

2) Proposer une fonction permettant d'insérer un élément dans un ABR. Quelle est la complexité de cette fonction ?

3) En déduire une fonction permettant de créer un ABR à partir de la liste des éléments qui le composera.

4) Proposer une variante de la fonction d'insertion qui n'ajoute pas l'élément x à l'arbre a s'il est déjà dedans.

5) Dans un ABR, où se trouve le plus petit élément? En déduire une fonction minimum(a) qui renvoie le plus petit élément de l'ABR a. Si l'arbre a est vide, alors cette fonction renvoie None.

6) Écrire une fonction compte(x, a) qui renvoie le nombre d'oсcurrences de x dans l'ABR a.