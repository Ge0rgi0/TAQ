# 🌐 SNT – Internet  

---

## Internet = un réseau de réseaux
Internet n’est pas une seule machine géante.  
C’est en réalité **un immense ensemble de réseaux interconnectés** :  

- **Les réseaux locaux (LAN)**  
  - Exemple : votre maison (box Internet + ordinateurs + téléphones connectés en Wi-Fi ou en câble).  
  - Exemple : le réseau du lycée (salles informatiques, imprimantes, serveurs pédagogiques).  
  - Exemple : le réseau d’une entreprise.  

Ces réseaux sont **privés et limités dans l’espace** (on les appelle des **réseaux locaux**).

---

### Les Fournisseurs d’Accès à Internet (FAI)
Pour communiquer avec le reste du monde, un réseau local doit se connecter à un **Fournisseur d’Accès à Internet (FAI)** :  
- En France : Orange, SFR, Free, Bouygues, etc.  
- Dans d’autres pays : AT&T, Deutsche Telekom, etc.  

Un FAI gère un **réseau beaucoup plus vaste** qui relie des millions de clients.  

---

### L’interconnexion mondiale
- Les réseaux des FAI sont eux-mêmes reliés **entre eux** par de très grandes lignes de communication (fibre optique, câbles sous-marins, satellites).  
- Les grandes entreprises (Google, Amazon, Microsoft, etc.) possèdent aussi leurs **propres réseaux** qui s’interconnectent avec les FAI.  

📌 Résultat :  
Quand vous envoyez un message, il sort d’abord de votre réseau local → passe par le réseau de votre FAI → traverse plusieurs autres réseaux → atteint le réseau du destinataire.  


👉 **Idée clé à retenir :**  
Internet, c’est **l’interconnexion de milliers de réseaux locaux et de fournisseurs d’accès** à l’échelle mondiale, qui communiquent tous grâce à des **protocoles communs**.

---

## Repères historiques
- **1950s-1960s** : premiers réseaux d’ordinateurs.  
- **1970** : ArpaNet (USA).  
- **1971** : Cyclades (France).  
- **1983** : naissance officielle d’Internet avec le protocole **TCP/IP**.  

---

## Le protocole IP et l’adressage

Chaque appareil connecté à Internet doit être identifiable de manière **unique**.  
Pour cela, deux types d’adresses existent :

---

### 📍 Adresse MAC (adressage local)
- Chaque machine dispose d’une ou plusieurs **cartes réseau** (Wi-Fi, Ethernet…).  
- Chaque carte possède une **adresse physique unique au monde** : l’adresse **MAC**.  
- Utilisée uniquement **dans le réseau local** (LAN).  

**Caractéristiques :**
- Format : 6 blocs de 2 caractères (ex. `a1:b2:c3:d4:e5:f6`).  
- Base : hexadécimale (0-9 et A-F).  
- Portée : limitée au réseau local.  
- Unicité : chaque carte réseau possède une adresse MAC unique.  

💡 Exemple :  

Adresse MAC = 3C:97:0E:4B:62:A1


---

### 🌐 Adresse IP (adressage global)
Pour communiquer sur Internet, chaque machine reçoit aussi une **adresse IP**.  
C’est l’adresse **logique** qui permet de retrouver une machine parmi des milliards d’autres.  

**Caractéristiques :**
- Format : 4 nombres entre 0 et 255 (ex. `192.168.1.12`).  
- Base humaine : décimale (base 10).  
- Base machine : binaire (0 et 1).  
- Portée : mondiale (Internet).  

💡 Exemples :  
- `91.198.174.192` (serveur de Wikipedia en IPv4).  
- `2a02:ec80:600:ed1a::1` (même serveur en IPv6).  
- `127.0.0.1` → adresse spéciale « localhost » (votre propre machine).  

---

### 🧩 Structure d’une adresse IP

Une **adresse IP** identifie une machine sur un réseau.  
Elle se compose de deux parties principales :  

1. **Partie Réseau** → identifie le réseau auquel appartient la machine.  
2. **Partie Machine (hôte)** → identifie la machine dans ce réseau.  

📌 Pour séparer ces deux parties, on utilise un **masque de sous-réseau**.

---

### IPv4 (Internet Protocol version 4)
- Format : **32 bits**, affichés en 4 nombres décimaux (0-255) séparés par des points.  
- Exemple : `128.40.94.3`  
- Masque : `/16` = `255.255.0.0`  
- En binaire :  

    Adresse : 10000000.00101000.01011110.00000011  
    Masque : 11111111.11111111.00000000.00000000

- Partie réseau : `128.40.0.0`  
- Partie machine : `94.3`  
- Portée : **Internet mondial**  
- Limitation : environ 4 milliards d’adresses → problème avec le nombre croissant d’appareils connectés.  

---

### IPv6 (Internet Protocol version 6)
- Créé pour résoudre la **pénurie d’adresses IPv4**.  
- Format : **128 bits**, représenté en **8 groupes de 4 caractères hexadécimaux** séparés par des deux-points.  
- Exemple : `2a02:ec80:600:ed1a::1`  
- Portée : mondiale, permet **un nombre quasi infini d’adresses**.  
- Partie réseau / partie machine : toujours présentes, mais sur un format plus long.  

---

### Comparatif IPv4 / IPv6

| Caractéristique   | IPv4                     | IPv6                               |
|------------------|-------------------------|-----------------------------------|
| Taille           | 32 bits                  | 128 bits                           |
| Format           | 4 nombres décimaux       | 8 blocs hexadécimaux               |
| Exemple          | 192.168.1.25             | 2a02:ec80:600:ed1a::1              |
| Nombre d’adresses| ~4 milliards             | 340 undecillions (~3,4×10³⁸)       |
| Objectif         | Adressage mondial limité | Résoudre la pénurie IPv4           |

---

💻 Expérience : découvrir les adresses IP et le réseau local de ton ordinateur

- Ouvrir l’invite de commande.
- Taper : ipconfig
- Observer :
  - Ton adresse IPv4 et IPv6
  - L’adresse de la passerelle (routeur)
  - Les serveurs DNS

---

### 📌 À retenir
- Une machine peut avoir **IPv4 et IPv6** simultanément.  
- La **partie réseau** permet de savoir si deux machines sont dans le même réseau local.  
- Le **masque de sous-réseau** détermine quelle partie de l’adresse est réseau et quelle partie est machine.

---

### 📊 Résumé comparatif
| Caractéristique  | Adresse MAC                         | Adresse IP                        |
|------------------|-------------------------------------|-----------------------------------|
| Nature           | Physique (gravée sur la carte)      | Logique (attribuée par le réseau) |
| Format           | 6 blocs hexadécimaux (ex. A1:B2:...)| 4 nombres décimaux (IPv4) ou longs hexadécimaux (IPv6) |
| Portée           | Réseau local                        | Réseau mondial (Internet)         |
| Unicité          | Unique au monde                     | Unique dans un réseau donné       |
| Exemple          | 3C:97:0E:4B:62:A1                   | 192.168.1.12                      |

---

📌 **À retenir :**  
- L’adresse **MAC** identifie la **carte réseau dans un LAN**.  
- L’adresse **IP** identifie l’**appareil sur Internet**.  
- Les deux sont nécessaires pour qu’un ordinateur puisse communiquer.


---

## DNS – Domain Name System

Quand vous tapez un nom de site dans votre navigateur, par exemple `wikipedia.org`, votre ordinateur ne sait pas directement où envoyer les paquets.  
Il a besoin de **l’adresse IP** correspondante.  

Le **DNS (Domain Name System)** est un service qui fait la correspondance :  

- Nom symbolique → Adresse IP  
- Exemple : `wikipedia.org` → `91.198.174.192` (IPv4) ou `2a02:ec80:600:ed1a::1` (IPv6)

Les **serveurs DNS** sont des ordinateurs spécialisés qui répondent aux requêtes des ordinateurs pour résoudre ces noms.  
Chaque ordinateur dispose d’un **serveur DNS configuré** (souvent celui de votre FAI) pour interroger le réseau.

📌 **À retenir :** sans DNS, il faudrait connaître l’adresse IP exacte de chaque site pour s’y connecter.

---

## Le protocole TCP (Transmission Control Protocol)

Quand on envoie un message ou un fichier sur Internet, **il n’est jamais envoyé d’un seul bloc**, mais découpé en **petits morceaux appelés paquets**.  

Chaque paquet contient :  
- l’adresse de l’**émetteur** (source),  
- l’adresse du **destinataire**,  
- une partie des **données** (texte, image, son…).  

| Adresse source | Adresse destination | Données |  
|----------------|---------|------------------|  

---

### 📌 Rôle de TCP
TCP est un **protocole de communication fiable**. Il s’assure que :  
1. **Tous les paquets arrivent à destination**.  
   - Si un paquet est perdu sur le chemin, TCP le redemande.  
2. **Les paquets sont remis dans le bon ordre**.  
   - Les paquets peuvent arriver dans le désordre, TCP les réorganise.  
3. **La congestion du réseau est gérée**.  
   - TCP ajuste la vitesse d’envoi pour ne pas saturer le réseau.  

💡 **Exemple concret :**  
- Vous regardez une vidéo en streaming :  
  - La vidéo est envoyée en milliers de paquets.  
  - TCP s’assure que chaque image arrive et est **reconstituée dans le bon ordre**.  

---

### 🔄 Transmission et fiabilité
- Chaque paquet contient un **numéro d’ordre** et un **accusé de réception (ACK)**.  
- Si un paquet n’est pas accusé dans un certain délai, il est **renvoyé automatiquement**.  

Ordinateur A ---> paquet #1 ---> Ordinateur B  
<--- ACK #1 ----  
Ordinateur A ---> paquet #2 ---> Ordinateur B  
<--- ACK #2 ----  


- Cela garantit que **tout le message est complet** à l’arrivée.  

---

### ⚠️ Limites de TCP
- TCP **ne garantit pas le temps d’arrivée** des paquets.  
  - Utile pour mails ou fichiers.  
  - Moins adapté pour les **vidéos en direct ou jeux en ligne**, car attendre les paquets manquants crée du **lag**.  
- Pour ces usages, on utilise souvent **UDP (User Datagram Protocol)**, qui envoie les paquets sans vérification ni réordonnancement → plus rapide mais moins fiable.

---

💻 Expérience : tester si un autre appareil ou site est joignable

- Ouvrir l’invite de commande.
- Taper : ping wikipedia.org
- Observer :
  - L’adresse IP de wikipedia.org
  - Le temps aller-retour des paquets
  - Si tous les paquets sont reçus


---

### 📌 À retenir
- TCP découpe les données en **paquets**, les envoie et les réassemble.  
- Il assure **la fiabilité** : tout paquet perdu est renvoyé et les paquets sont remis dans le bon ordre.  
- TCP est le protocole utilisé pour la majorité des communications **fiables** sur Internet (mail, web, transfert de fichiers).  
- Pour les applications **temps réel** (streaming, jeux), UDP est utilisé à la place.

---

## Le routage
Les paquets ne vont pas directement de l’émetteur au destinataire.  
Ils passent par plusieurs **routeurs**, qui choisissent à chaque étape le **meilleur chemin possible**.  

Schéma simplifié :  

Ordinateur A → [Routeur 1] → [Routeur 2] → [Routeur 3] → Ordinateur B


- Chaque routeur connaît seulement une **carte locale**.  
- Si un chemin est bloqué, le paquet est envoyé ailleurs.  
- Certains paquets peuvent être perdus → TCP les renvoie.  

💻 Expérience : suivre le chemin des paquets sur Internet

- Ouvrir l’invite de commande.
- Taper : tracert wikipedia.org
- Observer :
  - Les routeurs traversés
  - Les temps de passage
  - Les étoiles (*) pour routeurs qui ne répondent pas

---

### 🔹 Expérience pratique : nslookup

💻 **Objectif :** résoudre un nom de domaine en adresse IP et identifier le serveur DNS utilisé

1. Ouvrir l’invite de commande sur Windows.  
2. Taper la commande :

nslookup wikipedia.org  


3. Observer :
   - L’**adresse IP** retournée pour wikipedia.org
   - Le **serveur DNS** qui a répondu

4. Comparer avec l’adresse IP obtenue avec `ping wikipedia.org` pour voir que c’est la même.

💡 **Lien avec le cours :** cette expérience montre **comment un nom de site est traduit en adresse IP** avant que les paquets soient envoyés.


## Les composants matériels d’un réseau

Pour qu’un réseau fonctionne, plusieurs **éléments matériels** sont nécessaires :  

### 💻 1. Machines
- Ce sont les appareils qui **communiquent entre eux** :  
  - Ordinateurs, tablettes, smartphones, consoles de jeu, serveurs.  
- Elles envoient et reçoivent des données via le réseau.

### 🔀 2. Switch
- Dispositif qui **relie plusieurs machines localement** dans un réseau (LAN).  
- Exemple : un switch dans une salle informatique permet aux ordinateurs de communiquer entre eux rapidement.  
- Fonction : reçoit un paquet sur un port et l’envoie **uniquement au port correspondant à la machine destinataire**.

### 🌐 3. Routeur
- Permet de **connecter un réseau local à Internet** ou à d’autres réseaux.  
- Exemple : la box Internet à la maison est un routeur.  
- Fonction : **acheminer les paquets** entre les différents réseaux selon leur adresse IP.

### 📡 4. Supports de transmission
- Permettent de **transporter physiquement les données** entre machines et équipements réseau.  
- Types :  
  - **Câbles Ethernet** (filaire, stable et rapide)  
  - **Wi-Fi** (sans fil, pratique mais plus sensible aux interférences)  
  - **Fibre optique** (très haut débit, longue distance)  

---

## Modèle en couches TCP/IP

Le protocole TCP/IP organise la communication en **4 couches**, chacune ayant un rôle spécifique :  

**1 Couche Application** 📱  

Utilisée par les logiciels : navigateur web, messagerie, jeux en ligne.  
Contient les **données utilisateur**.
  
**2 Couche Transport** 🚛  

Assure le **transport fiable des données**.  
Garantit que les paquets arrivent complets et dans le bon ordre (TCP).  
  
**3 Couche Internet** 🗺️  

Gère **l’adressage et le routage**.  
Détermine le **chemin optimal** pour les paquets vers leur destination.
  
**4 Couche Accès Réseau** 🔌  

Assure la **transmission physique des données** : signaux électriques, optiques ou radio.  
Utilise les supports de transmission (Ethernet, Wi-Fi, fibre).  

---

### Encapsulation et désencapsulation

Quand une machine envoie des données :  

Les données descendent les couches **en se faisant encapsuler** → chaque couche ajoute son **en-tête**.  

📱 Application : données utilisateur  
⬇️  
🚛 Transport : + en-tête TCP  
⬇️  
🗺️ Internet : + en-tête IP  
⬇️  
🔌 Accès réseau : + en-tête Ethernet  
  

À la réception, les données remontent les couches **en se faisant désencapsuler** → chaque couche retire son en-tête pour récupérer les informations originales.  

🔌 Accès réseau : - en-tête Ethernet  
⬆️  
🗺️ Internet : - en-tête IP  
⬆️  
🚛 Transport : - en-tête TCP  
⬆️  
📱 Application : données utilisateur  

💡 **À retenir :**  
- L’encapsulation permet à chaque couche de **gérer ses propres fonctions** sans se préoccuper des autres.  
- La désencapsulation permet de **reconstituer les données correctement** à l’arrivée.