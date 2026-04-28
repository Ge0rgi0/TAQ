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

```
    A --- B
    |     |
    C --- D
```

Ici, `A`, `B`, `C`, `D` sont les **sommets**, et les traits sont les **arêtes**.

### Vocabulaire

- Le **degré** d'un sommet est le nombre d'arêtes qui lui sont reliées. Dans l'exemple ci-dessus, chaque sommet a un degré de 2.
- Deux sommets reliés par une arête sont dits **voisins** ou **adjacents**.
- Un **chemin** est une suite de sommets reliés les uns aux autres.
- Un **cycle** est un chemin qui revient à son point de départ.
- Un graphe est dit **connexe** s'il existe un chemin entre toute paire de sommets.

### Exercice

Soit le graphe suivant :

```
    A --- B --- E
    |     |
    C --- D
```

1) Quel est le degré de chaque sommet ?  
2) Donner un chemin de `A` à `E`.  
3) Ce graphe contient-il un cycle ? Si oui, lequel ?  
4) Ce graphe est-il connexe ?  

---

## Graphes orientés

Dans un graphe **orienté**, les arêtes (qu'on appelle alors des **arcs**) ont un sens, représenté par une flèche.

```
    A --> B
    ^     |
    |     v
    C <-- D
```

Si un arc va de `A` vers `B`, on dit que :

- `B` est un **successeur** de `A`
- `A` est un **prédécesseur** de `B`

> Exemple : les abonnements sur un réseau social. Je peux suivre quelqu'un sans qu'il me suive en retour.

### Exercice

1) Dans le graphe orienté ci-dessus, donner les successeurs et les prédécesseurs de chaque sommet.

2) Modéliser les situations suivantes. Pour chacune, préciser si le graphe est orienté ou non, et identifier les sommets et les arêtes :

   a) Un réseau de métro avec ses stations et ses lignes.

   b) Les pages d'un site web avec leurs liens hypertextes.

   c) Un tournoi de football où chaque équipe joue contre toutes les autres.

---

## Représentation par matrice d'adjacence

Pour manipuler un graphe en Python, il faut le représenter en mémoire. La première façon est la **matrice d'adjacence**.

On crée un tableau à deux dimensions de taille `n × n` (où `n` est le nombre de sommets). On numérote les sommets de `0` à `n-1`.

- `matrice[i][j] = 1` s'il existe une arête de `i` vers `j`
- `matrice[i][j] = 0` sinon

```
Graphe :             Matrice d'adjacence :
                        0  1  2  3
    0 --- 1           0[0, 1, 1, 0]
    |                 1[1, 0, 0, 1]
    2 --- 3           2[1, 0, 0, 1]
                      3[0, 1, 1, 0]
```

```python
matrice = [
    [0, 1, 1, 0],  # sommet 0
    [1, 0, 0, 1],  # sommet 1
    [1, 0, 0, 1],  # sommet 2
    [0, 1, 1, 0],  # sommet 3
]
```

Pour savoir si les sommets `i` et `j` sont voisins, il suffit de lire `matrice[i][j]`.

> **Avantage** : tester si deux sommets sont voisins est immédiat.  
> **Inconvénient** : on réserve `n²` cases en mémoire, même si le graphe a très peu d'arêtes.

### Exercice

1) Dessiner le graphe correspondant à la matrice suivante (les sommets sont numérotés 0, 1, 2, 3) :

```python
matrice = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
]
```

2) Cette matrice est-elle symétrique ? Qu'est-ce que cela signifie pour le graphe ?

3) Écrire une fonction `sont_voisins(matrice, i, j)` qui renvoie `True` si les sommets `i` et `j` sont voisins.

4) Écrire une fonction `degre(matrice, i)` qui renvoie le degré du sommet `i`.

5) Écrire une fonction `voisins(matrice, i)` qui renvoie la liste des voisins du sommet `i`.

---

## Représentation par liste d'adjacence

La deuxième représentation utilise un **dictionnaire** : chaque sommet est associé à la liste de ses voisins (ou successeurs dans le cas orienté).

```python
# Graphe non orienté
graphe = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
}
```

```python
# Graphe orienté : A --> B --> D <-- C --> A
graphe_oriente = {
    'A': ['B'],
    'B': ['D'],
    'C': ['A', 'D'],
    'D': [],
}
```

> **Avantage** : économique en mémoire, surtout quand le graphe a peu d'arêtes.  
> **Inconvénient** : pour savoir si deux sommets sont voisins, il faut parcourir toute leur liste.

### Exercice

1) Dessiner le graphe non orienté représenté par le dictionnaire suivant :

```python
graphe = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
}
```

2) Écrire une fonction `sont_voisins(graphe, u, v)` qui renvoie `True` si `u` et `v` sont voisins dans ce graphe.

3) Écrire une fonction `degre(graphe, u)` qui renvoie le degré du sommet `u`.

4) Écrire une fonction `matrice_vers_liste(matrice)` qui convertit une matrice d'adjacence (avec des sommets numérotés) en dictionnaire d'adjacence.

5) Écrire la fonction inverse : `liste_vers_matrice(graphe, sommets)` où `sommets` est la liste ordonnée des sommets.

---

## Parcours de graphes

Comme pour les arbres, on peut **parcourir** tous les sommets d'un graphe. Mais attention : un graphe peut contenir des **cycles**. Il faut donc mémoriser les sommets déjà visités pour ne pas boucler indéfiniment.

### Parcours en profondeur (DFS)

On explore une branche aussi loin que possible avant de revenir en arrière. C'est le même principe que le parcours en profondeur d'un arbre.

```python
def dfs(graphe, depart):
    visites = set()

    def explorer(s):
        if s in visites:
            return
        visites.add(s)
        print(s)
        for voisin in graphe[s]:
            explorer(voisin)

    explorer(depart)
```

### Parcours en largeur (BFS)

On explore tous les voisins d'un sommet avant de passer au niveau suivant. On utilise une **file**.

```python
from collections import deque

def bfs(graphe, depart):
    visites = set()
    file = deque([depart])
    visites.add(depart)

    while file:
        s = file.popleft()
        print(s)
        for voisin in graphe[s]:
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

### Exercice

Soit le graphe suivant :

```python
graphe = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
}
```

1) Dessiner ce graphe.

2) Donner l'ordre de visite des sommets lors d'un parcours DFS depuis `A`.

3) Donner l'ordre de visite des sommets lors d'un parcours BFS depuis `A`.

4) Écrire une fonction `est_connexe(graphe)` qui renvoie `True` si le graphe est connexe. *(Indication : après un parcours depuis n'importe quel sommet, tous les sommets doivent avoir été visités.)*

5) Écrire une fonction `chemin(graphe, depart, arrivee)` qui renvoie une liste de sommets formant un chemin entre `depart` et `arrivee`, ou `None` s'il n'en existe pas.