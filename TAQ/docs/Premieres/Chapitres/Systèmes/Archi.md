# Architecture des ordinateurs

## Qu'est-ce qu'une machine ?

Un ordinateur, c'est avant tout un ensemble de composants électroniques qui
travaillent ensemble. Mais comment ? Qui fait quoi ? Comment les informations
circulent-elles ?

Pour répondre à ces questions, les informaticiens utilisent un **modèle**,
c'est-à-dire une représentation simplifiée de la réalité. Le modèle le plus
célèbre est celui proposé par **John von Neumann** en 1945.

---

## Le modèle de Von Neumann

### L'idée fondamentale

Avant Von Neumann, les machines étaient **câblées** pour effectuer une tâche
précise. Changer de tâche signifiait recâbler physiquement la machine. C'était
long, coûteux, et peu pratique.

Von Neumann propose une idée révolutionnaire : et si on stockait le **programme
en mémoire**, au même endroit que les données ? La machine pourrait alors
exécuter n'importe quel programme, juste en changeant ce qu'elle lit en mémoire.

C'est le principe de l'**ordinateur à programme enregistré**, et c'est encore
le principe de tous les ordinateurs modernes.

### Les 4 composants

Le modèle de Von Neumann décompose l'ordinateur en **4 éléments** :

![Von Neumann](VonN.png)

#### 1. Le processeur (CPU)

C'est le **cerveau** de l'ordinateur. Il lit les instructions du programme et
les exécute. Il se divise lui-même en deux parties :

- **L'Unité de Contrôle (UC)** : elle lit les instructions en mémoire et
  coordonne le travail des autres composants. C'est elle qui décide "quelle
  est la prochaine instruction à exécuter ?"
- **L'Unité Arithmétique et Logique (UAL)** : elle effectue tous les calculs
  (additions, soustractions...) et les opérations logiques (comparaisons,
  ET, OU...).

#### 2. La mémoire

C'est là que sont stockés **les programmes ET les données** pendant l'exécution.
C'est le principe clé de Von Neumann : tout est dans la même mémoire.

On peut imaginer la mémoire comme une très longue liste de cases numérotées.
Chaque case contient une valeur (une instruction ou une donnée), et chaque case
a une **adresse** unique.

#### 3. Les entrées/sorties

Ce sont les composants qui permettent à l'ordinateur de **communiquer avec
l'extérieur** :

- **Entrées** : clavier, souris, capteurs, microphone, webcam...
- **Sorties** : écran, haut-parleurs, imprimante...

Sans entrées/sorties, un ordinateur ne pourrait ni recevoir d'informations ni
en communiquer.

#### 4. Le bus

Ce n'est pas vraiment un composant isolé, mais c'est ce qui **relie tout le
reste**. Le bus est un ensemble de fils électriques qui permettent aux
composants d'échanger des données.

On distingue généralement :

- le **bus de données** : transporte les données
- le **bus d'adresses** : indique où lire ou écrire en mémoire

---

## Le langage machine

### Les registres

Pour effectuer ses calculs, le processeur dispose de petites zones de
stockage ultrarapides appelées **registres**. On peut les voir comme des
**variables internes** au processeur.

Contrairement à la mémoire (grande mais lente), les registres sont en
nombre limité (une dizaine en général) mais accessibles instantanément.

On les nomme généralement A, B, C... ou R0, R1, R2...

### Le Compteur de Programme (CP)

Le processeur dispose d'un registre spécial : le **Compteur de Programme**
(CP). Il contient en permanence **l'adresse de la prochaine instruction
à exécuter**.

À chaque instruction exécutée, le CP s'incrémente automatiquement pour
passer à la suivante. C'est lui qui donne au processeur sa progression dans
le programme.

### Les instructions de base

Un programme en langage machine est une suite d'instructions très simples.
En voici les principales :

| Instruction | Signification |
|---|---|
| `LOAD R, valeur` | Charge une valeur dans le registre R |
| `LOAD R, @adresse` | Charge en R la valeur stockée à cette adresse mémoire |
| `STORE R, @adresse` | Copie la valeur de R vers cette adresse mémoire |
| `ADD R1, R2` | Additionne R1 et R2, stocke le résultat dans R1 |
| `SUB R1, R2` | Soustrait R2 à R1, stocke le résultat dans R1 |
| `JUMP @adresse` | Le CP saute à cette adresse (rupture de séquence) |
| `HALT` | Arrête le programme |

### Exemple de programme

On souhaite calculer 8 - 3 et stocker le résultat à l'adresse mémoire 10.

| Adresse | Instruction | Ce qui se passe |
|---|---|---|
| 0 | `LOAD A, 8` | A ← 8, CP passe à 1 |
| 1 | `LOAD B, 3` | B ← 3, CP passe à 2 |
| 2 | `SUB A, B` | A ← 8 - 3 = 5, CP passe à 3 |
| 3 | `STORE A, @10` | La valeur 5 est écrite à l'adresse 10, CP passe à 4 |
| 4 | `HALT` | Le programme s'arrête |

À la fin de l'exécution :

- Le registre A contient **5**
- L'adresse mémoire 10 contient **5**
- Le CP vaut **4**

<span style="color:red">Exercices</span>

**1.** Dérouler le programme suivant instruction par instruction.
Indiquer à chaque étape la valeur du CP et le contenu des registres.

| Adresse | Instruction |
|---|---|
| 0 | `LOAD A, 10` |
| 1 | `LOAD B, 4` |
| 2 | `ADD A, B` |
| 3 | `LOAD B, 2` |
| 4 | `SUB A, B` |
| 5 | `STORE A, @20` |
| 6 | `HALT` |

*Que contient l'adresse mémoire 20 à la fin ?*

**2.** On dispose de la mémoire suivante :

| Adresse | Valeur |
|---|---|
| 5 | 12 |
| 6 | 7 |

Dérouler le programme :

| Adresse | Instruction |
|---|---|
| 0 | `LOAD A, @5` |
| 1 | `LOAD B, @6` |
| 2 | `ADD A, B` |
| 3 | `STORE A, @7` |
| 4 | `HALT` |

*Que contient l'adresse mémoire 7 à la fin ?*

**3.** Écrire un programme en langage machine qui calcule 3 + 5 + 2
et stocke le résultat à l'adresse mémoire 15.

**4.** Que fait ce programme ? Expliquer son effet.

| Adresse | Instruction |
|---|---|
| 0 | `LOAD A, 1` |
| 1 | `ADD A, A` |
| 2 | `STORE A, @0` |
| 3 | `HALT` |

**5.** On souhaite calculer le périmètre d'un rectangle de longueur 8
et de largeur 3. Le périmètre vaut 2 × (longueur + largeur).

Écrire un programme en langage machine qui :
- calcule ce périmètre
- stocke le résultat à l'adresse mémoire 20

---

## La mémoire en détail

### Mémoire vive (RAM)

La **RAM** (Random Access Memory) est la mémoire principale de l'ordinateur.
C'est là que sont chargés les programmes et les données **en cours
d'utilisation**.

- Elle est **rapide** : le processeur peut y accéder en quelques nanosecondes.
- Elle est **volatile** : son contenu **disparaît** quand on coupe
  l'alimentation.
- Sa capacité se mesure en **Gio** (gibioctets) sur les machines modernes.

### Mémoire morte (ROM)

La **ROM** (Read Only Memory) est une mémoire **non volatile** : son contenu
est conservé même sans alimentation, mais elle ne peut pas être modifiée
(ou très difficilement).

Elle contient en général les instructions de démarrage de la machine
(le **BIOS** ou l'**UEFI**).

### Le stockage permanent (SSD, disque dur)

Le **SSD** (Solid State Drive) ou le disque dur permettent de stocker des
données **de façon permanente** : fichiers, programmes, système d'exploitation...

- Beaucoup plus **lent** que la RAM
- Beaucoup plus **grand** (des centaines de Gio, voire des Tio)
- **Non volatile** : les données survivent à l'extinction

### Les unités de mesure

| Unité | Symbole | Valeur approximative |
|-------|---------|----------------------|
| Octet | o | 1 caractère |
| Kibioctet | Kio | 1 024 octets |
| Mébioctet | Mio | 1 024 Kio |
| Gibioctet | Gio | 1 024 Mio |
| Tébioctet | Tio | 1 024 Gio |

> **Attention :** On voit souvent Go (gigaoctet = 10⁹ octets) dans les
> publicités, et Gio (gibioctet = 2³⁰ octets) en informatique. Ce ne sont
> pas exactement les mêmes valeurs.

---

## Monoprocesseur et multiprocesseur

### Monoprocesseur

Un ordinateur **monoprocesseur** possède un seul cœur de calcul. Il ne peut
exécuter qu'**une seule instruction à la fois**.

Quand plusieurs programmes semblent tourner en même temps (musique +
navigateur + traitement de texte), c'est en réalité le système d'exploitation
qui **alterne très rapidement** entre les programmes, si vite que l'utilisateur
a l'impression de simultanéité.

### Multiprocesseur

Un ordinateur **multiprocesseur** (ou multi-cœurs) possède plusieurs unités
de calcul. Il peut exécuter **réellement plusieurs instructions en parallèle**.

Les processeurs modernes ont généralement 4, 8, voire 16 cœurs ou plus.

---

## Le SoC (System on Chip)

Un **SoC** (System on Chip, ou "système sur une puce") est un circuit intégré
qui rassemble **tous les composants d'un ordinateur sur une seule puce** :
processeur, mémoire, GPU, interfaces réseau, etc.

![](soc.png)

**Exemples :** Raspberry Pi, smartphones (Apple M1, Snapdragon...), montres
connectées, consoles portables.

### Avantages

- **Consommation électrique très faible** : idéal pour les appareils sur
  batterie
- **Encombrement réduit** : tout tient sur une puce de quelques centimètres
- **Coût de fabrication moins élevé**
- **Robustesse** : moins de connexions entre composants = moins de pannes

### Inconvénients

- **Difficile à réparer** : si un composant est défaillant, on change tout
- **Impossible à upgrader** : on ne peut pas changer la RAM ou le processeur
  séparément
- **Dissipation thermique complexe** : tout chauffe au même endroit
