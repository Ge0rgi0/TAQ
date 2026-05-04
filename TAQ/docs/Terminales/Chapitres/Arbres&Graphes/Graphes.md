# Graphes

## Introduction

Les arbres que nous avons étudiés sont des structures **hiérarchiques** : chaque nœud n'a qu'un seul parent, les relations vont toujours du parent vers l'enfant.

Mais de nombreuses situations réelles sont plus complexes :

- Dans un **réseau routier**, une ville peut être reliée à plusieurs autres, dans les deux sens.
- Dans un **réseau social**, une personne peut suivre ou être suivie par de nombreuses autres.
- Sur **Internet**, un serveur peut être connecté à des dizaines d'autres.

Pour modéliser ces situations, on utilise une structure plus générale : le **graphe**.

---

## Définitions

Un **graphe** est un ensemble de **sommets** reliés entre eux par des **arêtes**.

![](graph.png)

Ici, `A`, `B`, `C`, `D` sont les **sommets**, et les traits sont les **arêtes**.

### Vocabulaire

- Le **degré** d'un sommet est le nombre d'arêtes qui lui sont reliées. Dans l'exemple ci-dessus, chaque sommet a un degré de 2.
- Deux sommets reliés par une arête sont dits **voisins** ou **adjacents**.
- Un **chemin** est une suite de sommets reliés les uns aux autres.
- Un **cycle** est un chemin qui revient à son point de départ.
- Un graphe est dit **connexe** s'il existe un chemin entre toute paire de sommets.

### Exercice

Soit le graphe suivant :

![](exo1.png)

1) Quel est le degré de chaque sommet ?  
2) Donner un chemin de `A` à `E`.  
3) Ce graphe contient-il un cycle ? Si oui, lequel ?  
4) Ce graphe est-il connexe ?  

---

## Graphes orientés
 
Dans un graphe **orienté**, les arêtes (qu'on appelle alors des **arcs**) ont un sens, représenté par une flèche.
 
![](dir.png)
 
Si un arc va de `A` vers `B`, on dit que :
 
- `B` est un **successeur** de `A`
- `A` est un **prédécesseur** de `B`
> Exemple : les abonnements sur un réseau social. Je peux suivre quelqu'un sans qu'il me suive en retour.
 
Dans un graphe orienté, chaque arc ayant une direction, on distingue deux types de degrés pour un sommet :

- Degré sortant : nombre d'arcs qui partent du sommet.
- Degré entrant : nombre d'arcs qui arrivent vers le sommet.

### Chemins et cycles dans un graphe orienté
 
L'orientation des arcs change la notion de chemin : on ne peut désormais se déplacer **que dans le sens des flèches**.
 
Dans le graphe ci-dessus, il existe un chemin de `A` vers `C` (en passant par `B`), mais il n'en existe pas de `C` vers `A`.
 
De même, un **cycle** dans un graphe orienté doit respecter le sens des arcs. Un ensemble de sommets peut former un cycle dans un sens, mais pas dans l'autre.
 
### Exercice
 
1) Dans le graphe orienté ci-dessus, donner les successeurs et les prédécesseurs de chaque sommet.  

2) Existe-t-il un chemin de `A` vers `D` ? De `D` vers `A` ? Justifier.  

3) Ce graphe contient-il un cycle ? Si oui, lequel ?  

4) Modéliser chacune des situations suivantes sous forme de graphe en identifiant les sommets et les arêtes.
Pour chacun d'entre eux dire :
- s'il est connexe
- le degré de chaque sommet (indiqué les voisins ou predecessurs/successeurs)
- s'il est cyclique


**Situation A** — Le réseau ferroviaire d'une région comporte les liaisons suivantes :

- Paris est relié à Lyon, Bordeaux et Lille.
- Lyon est relié à Marseille et Grenoble.
- Bordeaux est relié à Toulouse.
- Lille est relié à Strasbourg.

**Situation B** — Sur un réseau social, voici les abonnements entre utilisateurs :

- Alice suit Bob et Clara.
- Bob suit Clara.
- Clara suit Alice.
- David suit Alice et Bob.

**Situation C** — Dans une entreprise, voici les liens hiérarchiques :

- La PDG dirige les responsables Marketing, Technique et Commercial.
- Le responsable Technique dirige les développeurs Alice et Bob.
- Le responsable Commercial dirige la commerciale Clara.

---

## Représentation par matrice d'adjacence

On peut représenter un graphe sous forme de tableau : les lignes et les colonnes correspondent aux sommets, et on indique `1` s'il existe une arête entre deux sommets, `0` sinon.

|   | A | B | C | D |
|---|---|---|---|---|
| A | 0 | 1 | 1 | 0 |
| B | 1 | 0 | 0 | 1 |
| C | 1 | 0 | 0 | 1 |
| D | 0 | 1 | 1 | 0 |

### Exercice

Soit le graphe suivant :

![](exo2.png)

1) Recopier et compléter la matrice d'adjacence de ce graphe.

2) Dessiner le graphe correspondant à la matrice suivante :

|   | A | B | C | D |
|---|---|---|---|---|
| A | 0 | 1 | 0 | 1 |
| B | 1 | 0 | 1 | 0 |
| C | 0 | 1 | 0 | 1 |
| D | 1 | 0 | 1 | 0 |

3) Comment pourrait-on reconnaitre un graphe non orienté, uniquement avec sa matrice d'adjacence ?

4) Comment lire le degré d'un sommet directement sur la matrice ?

---

## Représentation par liste d'adjacence

On peut aussi représenter un graphe sous forme d'un tableau à deux colonnes : pour chaque sommet, on liste ses voisins.

| Sommet | Voisins |
|--------|---------|
| A | B, C |
| B | A, D |
| C | A, D |
| D | B, C |

### Exercice

Soit le graphe suivant :

![](exo2.png)

1) Recopier et compléter le tableau de liste d'adjacence de ce graphe.

2) Dessiner le graphe correspondant au tableau suivant :

| Sommet | Voisins |
|--------|---------|
| A | B, D |
| B | A, C, D |
| C | B |
| D | A, B |

---

### Quelle représentation choisir ?

Le choix dépend du graphe et de ce qu'on veut en faire.

Si le graphe est **dense** (beaucoup d'arêtes) ou qu'on a souvent besoin de tester si deux sommets sont voisins, la **matrice** est plus adaptée : la réponse est immédiate.

Si le graphe est **creux** (peu d'arêtes par rapport au nombre de sommets), la **liste** est plus adaptée : inutile de réserver une case pour chaque paire de sommets qui ne sont pas reliés. Un réseau routier avec 100 villes reliées chacune à 3 ou 4 voisines occuperait 10 000 cases en matrice, pour seulement quelques centaines d'arêtes réelles.

En pratique, la liste d'adjacence est la représentation la plus courante, car la plupart des graphes réels sont creux.

---

## Parcours de graphes

Pour explorer un graphe, on doit visiter tous ses sommets exactement une fois. Contrairement aux arbres, un graphe peut contenir des **cycles** : il faut donc mémoriser les sommets déjà visités pour ne pas boucler indéfiniment.

### Parcours en profondeur (DFS — *Depth First Search*)

Comme pour les arbres, on explore une direction aussi loin que possible avant de revenir en arrière.

|Étapes|Graphe|Ont été traités|Actuel|À traiter|
|--|--|--|--|--|
|0|![](parcours_prof_0.png)|||0|
|1|![](parcours_prof_1.png)||0|1 2|
|2|![](parcours_prof_2.png)|0|1|5 2|
|3|![](parcours_prof_3.png)|0 1|5|2|
|4|![](parcours_prof_4.png)|0 1 5|2|3 4|
|5|![](parcours_prof_5.png)|0 1 5 2|3|4|
|6|![](parcours_prof_6.png)|0 1 5 2 3|4|6|
|7|![](parcours_prof_7.png)|0 1 5 2 3 4|6||
|Fin|![](parcours_prof_8.png)|0 1 5 2 3 4 6|||


**Ordre de visite : 0 1 5 2 3 4 6**

### Parcours en largeur (BFS — *Breadth First Search*)

On explore tous les voisins d'un sommet avant de passer au niveau suivant, comme une onde qui se propage.

|Étapes|Graphe|Ont été traités|Actuel|À traiter|
|--|--|--|--|--|
|0|![](parcours_prof_0.png)|||0|
|1|![](parcours_prof_1.png)||0|1 2|
|2|![](parcours_prof_2.png)|0|1|2 5|
|3|![](parcours_larg_3.png)|0 1|2|5 3 4|
|4|![](parcours_larg_4.png)|0 1 2|5|3 4|
|5|![](parcours_prof_5.png)|0 1 2 5|3|4|
|6|![](parcours_prof_6.png)|0 1 2 5 3|4|6|
|7|![](parcours_prof_7.png)|0 1 2 5 3 4|6||
|Fin|![](parcours_prof_8.png)|0 1 2 5 3 4 6|||

**Ordre de visite : 0 1 2 5 3 4 6**

### Composantes connexes

Un graphe n'est pas toujours connexe : il peut être composé de plusieurs "morceaux" isolés les uns des autres. Chacun de ces morceaux est appelé une **composante connexe**.

![](composantes.png)

Ce graphe a trois composantes connexes : `{A, B, C}`, `{D, E}` et `{F}`.

![](composantes_dir.png)

Ce graphe a deux composantes connexes : `{A, B, C, D}`, `{E, F}`.

Un parcours (DFS ou BFS) depuis un sommet `s` ne visitera que les sommets de la composante connexe de `s`, il est impossible d'atteindre un sommet qui n'y est pas relié. Pour parcourir un graphe entier non connexe, il faut donc relancer un parcours depuis un sommet non visité de chaque composante.

### Exercice

Soit le graphe suivant :

![](graphe_parcours.png)

1) Donner l'ordre de visite des sommets pour un parcours DFS depuis `A`.  
2) Donner l'ordre de visite des sommets pour un parcours BFS depuis `A`.   
3) Le résultat dépend-il de l'ordre dans lequel on considère les voisins de chaque sommet ?  

4) Quels sont les composantes connexes de ces graphes :
![](exo_comp.png)

---

## Exercices Python

On travaillera avec la représentation par liste d'adjacence suivante :

```python
class Graphe:
    def __init__(self):
        self.adjacence = {}

    def ajouter_sommet(self, s):
        if s not in self.adjacence:
            self.adjacence[s] = []

    def ajouter_arete(self, u, v):
        self.adjacence[u].append(v)
        self.adjacence[v].append(u)

    def voisins(self, s):
        return self.adjacence[s]

    def sommets(self):
        return list(self.adjacence.keys())
```

### Prise en main

1) Écrire une fonction `afficher(g)` qui affiche pour chaque sommet la liste de ses voisins.

2) Écrire une fonction `est_voisin(g, u, v)` qui renvoie `True` si `u` et `v` sont voisins.

3) Écrire une fonction `degre(g, s)` qui renvoie le degré du sommet `s`.

4) Écrire une fonction `sommet_max(g)` qui renvoie le sommet de plus haut degré.

5) Écrire une fonction `nb_aretes(g)` qui renvoie le nombre d'arêtes du graphe.

### Parcours

6) Écrire une fonction `dfs(g, depart)` qui affiche les sommets dans l'ordre d'un parcours en profondeur depuis `depart`.

7) Écrire une fonction `bfs(g, depart)` qui affiche les sommets dans l'ordre d'un parcours en largeur depuis `depart`.

8) Écrire une fonction `est_connexe(g)` qui renvoie `True` si le graphe est connexe. *(Indication : après un parcours depuis n'importe quel sommet, tous les sommets doivent avoir été visités.)*

9) Écrire une fonction `composantes(g)` qui renvoie la liste des composantes connexes du graphe. Chaque composante est une liste de sommets. *(Indication : relancer un parcours depuis chaque sommet non encore visité.)*

### Chemins

10) Écrire une fonction `chemin(g, depart, arrivee)` qui renvoie une liste de sommets formant un chemin entre `depart` et `arrivee`, ou `None` s'il n'en existe pas.

11) Écrire une fonction `distance(g, depart, arrivee)` qui renvoie le nombre d'arêtes du plus court chemin entre `depart` et `arrivee`, ou `None` s'il n'en existe pas. *(Indication : utiliser un BFS en mémorisant la distance à chaque sommet visité.)*

12) Écrire une fonction `sont_relies(g, u, v)` qui renvoie `True` si `u` et `v` sont dans la même composante connexe.

### Cycles

13) Écrire une fonction `contient_cycle(g)` qui renvoie `True` si le graphe contient au moins un cycle. *(Indication : lors d'un DFS, si on retombe sur un sommet déjà visité qui n'est pas le parent direct du sommet courant, c'est qu'il y a un cycle.)*

14) En déduire une fonction `est_arbre(g)` qui renvoie `True` si le graphe est un arbre. *(Rappel : un arbre est un graphe connexe sans cycle.)*

### Labyrinthe

On modélise un labyrinthe comme un graphe : chaque cellule est un sommet, et deux cellules adjacentes sans mur entre elles sont reliées par une arête.

```python
labyrinthe = {
    (0,0): [(0,1), (1,0)],
    (0,1): [(0,0)],
    (1,0): [(0,0), (1,1)],
    (1,1): [(1,0), (2,1)],
    (2,0): [(2,1)],
    (2,1): [(1,1), (2,0)],
}
```

15) L'entrée est `(0,0)` et la sortie est `(2,1)`. Utiliser la fonction `chemin` pour trouver un chemin entre l'entrée et la sortie.

16) Utiliser la fonction `distance` pour trouver le chemin le plus court.

17) Ce labyrinthe contient-il des cycles ? Qu'est-ce que cela signifie concrètement ?

## Outils

[Site de création de graphes](https://csacademy.com/app/graph_editor/)