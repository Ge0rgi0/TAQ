# Systèmes d'exploitation

## Qu'est-ce qu'un système d'exploitation ?

### Un peu d'histoire

Dans les années 1950, les premiers ordinateurs n'avaient **pas de système
d'exploitation**. Les programmeurs devaient tout gérer eux-mêmes : charger
leur programme en mémoire, piloter les composants, gérer les erreurs...
C'était long, fastidieux et réservé à des spécialistes.

Peu à peu, des programmes utilitaires ont été créés pour automatiser ces
tâches répétitives. Ces programmes se sont regroupés pour former ce qu'on
appelle aujourd'hui un **système d'exploitation**.

Les premiers systèmes d'exploitation apparaissent dans les années 1960 avec
les mainframes d'IBM. Dans les années 1980, l'arrivée des ordinateurs
personnels popularise des systèmes comme **MS-DOS** (Microsoft) puis
**Windows**. En 1991, un étudiant finlandais nommé **Linus Torvalds** publie
le noyau **Linux**, qui deviendra la base de nombreux systèmes libres.

![](history.png)

---

### Rôle d'un système d'exploitation

Un **système d'exploitation** (ou OS, de l'anglais *Operating System*) est
un ensemble de programmes qui fait l'**intermédiaire entre le matériel et
les logiciels**.

Sans lui, impossible de lancer une application, d'enregistrer un fichier ou
même d'afficher quelque chose à l'écran.

Ses principales fonctions sont :

- **Gérer les fichiers et répertoires** : organiser, lire, écrire, supprimer
les données sur les disques
- **Gérer les processus** : lancer, suspendre, arrêter les programmes en
cours d'exécution
- **Gérer les utilisateurs et les droits** : définir qui a accès à quoi
- **Gérer la mémoire** : allouer la RAM aux programmes qui en ont besoin
- **Gérer les entrées/sorties** : faire communiquer les programmes avec le
clavier, l'écran, le réseau...

> **Idée clé :** Sans OS, un ordinateur ne sait rien faire. C'est lui qui
> rend la machine utilisable.

---

## Logiciels libres et logiciels propriétaires

### Logiciels propriétaires

Un **logiciel propriétaire** est un logiciel dont le **code source est
fermé**. Seule l'entreprise qui l'a créé peut le modifier. L'utilisateur
achète une **licence** qui lui donne le droit de l'utiliser, mais pas de le
modifier ni de le redistribuer.

Exemples : **Windows**, **macOS**, **Microsoft Office**, **Photoshop**

### Logiciels libres

Un **logiciel libre** est un logiciel dont le **code source est ouvert**,
accessible à tous. N'importe qui peut le lire, le modifier et le
redistribuer librement.

Les 4 libertés fondamentales d'un logiciel libre (définies par la Free
Software Foundation) :
- Liberté d'**utiliser** le programme
- Liberté d'**étudier** son fonctionnement
- Liberté de le **modifier**
- Liberté de le **redistribuer**

Exemples : **Linux**, **LibreOffice**, **Firefox**, **VLC**

### Comparaison

| | Propriétaire | Libre |
|---|---|---|
| Code source | Fermé | Ouvert |
| Modification | Interdite | Autorisée |
| Prix | Souvent payant | Souvent gratuit |
| Exemples | Windows, macOS | Linux, LibreOffice |

> **Attention :** Gratuit ≠ libre. Un logiciel peut être gratuit sans être
> libre (ex : Spotify gratuit mais propriétaire). Et un logiciel libre peut
> être payant.

---

## L'arborescence de fichiers

### Structure en arbre

Sur un système Linux, les fichiers sont organisés selon une **structure
arborescente** : c'est une hiérarchie de **répertoires** (dossiers) et de
**fichiers**, qui part d'un point unique appelé la **racine**, notée `/`.

```
/
├── home/
│   ├── alice/
│   │   ├── documents/
│   │   │   └── rapport.txt
│   │   └── images/
│   │       └── photo.jpg
│   └── bob/
└── etc/
```

Chaque élément de l'arborescence est soit :
- un **répertoire** : contient d'autres fichiers ou répertoires
- un **fichier** : contient des données

### Chemin absolu

Un **chemin absolu** part toujours de la racine `/`. Il décrit la position
complète d'un fichier, peu importe où on se trouve.

Exemple : `/home/alice/documents/rapport.txt`

### Chemin relatif

Un **chemin relatif** part du **répertoire courant** (là où on se trouve
actuellement). Il utilise :
- `.` pour désigner le répertoire courant
- `..` pour désigner le répertoire parent (remonter d'un niveau)

Exemple : si on est dans `/home/alice/`, le chemin relatif vers
`rapport.txt` est `documents/rapport.txt`

Pour remonter vers `/home/` depuis `/home/alice/documents/` :
`../../`

### Lire l'invite de commande

Quand on ouvre un terminal sous Linux, on voit une ligne comme :

```
/
└── home/
└── elsa/
├── lycee/
│   ├── nsi/
│   │   └── tp1.py
│   └── maths/
│       └── cours.pdf
└── perso/
└── photo.jpg
```

**1.** Donner le chemin absolu du fichier `cours.pdf`.

**2.** On se trouve dans le répertoire `nsi`. Donner le chemin relatif
pour accéder à `photo.jpg`.

**3.** On se trouve dans le répertoire `elsa`. Donner deux façons
d'accéder au fichier `tp1.py` : une avec un chemin absolu, une avec un
chemin relatif.

**4.** Quelle est la différence entre `/home/elsa` et `~` quand on est
connecté en tant que `elsa` ?

---

## Premières commandes Linux

### Le terminal

Le **terminal** (ou console) est une interface en **ligne de commande** :
on tape du texte, la machine répond par du texte. C'est une façon directe
et puissante d'interagir avec le système.

Contrairement à une interface graphique, le terminal permet d'effectuer des
opérations précises, rapides et automatisables.

### Commandes de navigation

| Commande | Rôle | Exemple |
|---|---|---|
| `pwd` | Afficher le répertoire courant | `pwd` |
| `ls` | Lister le contenu du répertoire | `ls` |
| `cd chemin` | Changer de répertoire | `cd documents` |
| `cd ..` | Remonter d'un niveau | `cd ..` |
| `cd ~` | Aller dans son répertoire personnel | `cd ~` |
| `cat fichier` | Afficher le contenu d'un fichier | `cat notes.txt` |
| `man commande` | Afficher la documentation | `man ls` |

> **Astuce :** La touche `Tab` permet de compléter automatiquement un nom
> de fichier ou de répertoire. Les flèches ↑ et ↓ permettent de naviguer
> dans les commandes précédentes.

<span style="color:red">TP — Terminus</span>

Tu vas découvrir les commandes Linux en jouant à **Terminus**, un jeu
d'aventure en ligne de commande.

Rends-toi sur : **http://luffah.xyz/bidules/Terminus/**

- Accepte les cookies pour sauvegarder ta progression.
- Commence toujours par taper `ls` pour voir ce qui t'entoure.
- Utilise `cat` pour lire les objets et personnages.
- Utilise `cd` pour te déplacer.

Au fur et à mesure, **note dans un tableau** les nouvelles commandes que tu
découvres et leur rôle.

| Commande | Rôle |
|---|---|
| `ls` | ... |
| `cd` | ... |
| ... | ... |