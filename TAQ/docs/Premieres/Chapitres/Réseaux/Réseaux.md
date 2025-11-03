# Les Réseaux

## Histoire des réseaux de communication

### Les tours génoises

Au XVIᵉ siècle, sur les côtes méditerranéennes (notamment en Corse), on érigeait de grandes tours de pierre : les **tours génoises**. Leur rôle n’était pas décoratif, mais stratégique. Elles servaient à **prévenir les attaques de pirates**.

Les guetteurs, postés au sommet, communiquaient entre tours grâce à **des signaux visuels** : de la **fumée le jour**, du **feu la nuit**. Ainsi, un message pouvait parcourir des dizaines de kilomètres en quelques minutes. C’était déjà une forme de **réseau de communication**.

Mais ce réseau avait ses limites : il ne fonctionnait que **si la visibilité était bonne** et nécessitait **une vigilance permanente**. La communication restait donc lente, ponctuelle et tributaire de la météo.

![tour](tour.png)

---

### Les sémaphores et le télégraphe optique

Deux siècles plus tard, en pleine Révolution française, un ingénieur nommé **Claude Chappe** imagine un système plus fiable : le **télégraphe optique**, ou **sémaphore**. Chaque tour est équipée d’un grand mât muni de bras articulés. Selon leur position, ils forment des lettres ou des symboles que les opérateurs lisent à la longue-vue avant de les reproduire sur la tour suivante.

En 1794, Chappe parvient à transmettre un message de Paris à Lille en quelques minutes : une prouesse pour l’époque. La France se couvre alors d’un vaste réseau de tours, véritables ancêtres des relais de communication modernes.

Mais le système reste dépendant du jour et du beau temps.

![sem](sem.png)

---

### Le télégraphe électrique

Au milieu du XIXᵉ siècle, une révolution se prépare : l’électricité entre en scène. L’Américain **Samuel Morse** met au point un télégraphe capable d’envoyer des **impulsions électriques** à travers un fil métallique. Chaque impulsion correspond à un **point** ou un **trait** : c’est le **code Morse**. Grâce à lui, les messages peuvent être transmis **en temps réel sur des centaines de kilomètres**. En 1858, le premier **câble transatlantique** relie l’Europe à l’Amérique. Le monde commence à se rétrécir.

![tl](tl.png)

---

### Le téléphone

En 1876, **Alexander Graham Bell** dépose le brevet du **téléphone**. Pour la première fois, la voix humaine traverse les fils électriques. Les signaux ne sont plus codés : ils deviennent **sonores**.

Le téléphone change la société. Les distances s’effacent, les conversations deviennent immédiates, les relations commerciales s’accélèrent. C’est le premier véritable réseau mondial de communication **interpersonnelle**, celui des lignes téléphoniques.

![](phone.png)

---

### ARPANET

En 1969, au cœur de la guerre froide, les États-Unis cherchent un moyen de relier leurs ordinateurs pour **échanger des informations même en cas d’attaque**. La **DARPA**, agence du ministère de la Défense, crée **ARPANET**.

Ce réseau relie quatre universités américaines : UCLA, Stanford, Santa Barbara et Utah. Les chercheurs y testent une idée nouvelle : **la commutation de paquets**, qui consiste à découper les données en petits morceaux indépendants. Ce principe, toujours utilisé aujourd’hui, est à la base d’**Internet**.

Le premier message envoyé devait être « LOGIN »… mais le système s’est arrêté après deux lettres. Le premier mot d’Internet fut donc simplement **“LO”** .

![](ARPANET.png)

---

### Le Minitel

Dans les années 1980, la France développe son propre réseau numérique : le **Minitel**. C’est un petit terminal branché sur la ligne téléphonique qui permet d’accéder à des services en ligne : annuaires, messageries, réservations, banques, petites annonces…

Bien avant Internet, le Minitel met des millions de Français en contact avec le monde numérique. C’est un **précurseur du Web**, avec son interface textuelle et son système d’adresses, comme le fameux « 3615 ».

![](minitel.png)

---

## Internet

<iframe width="400" height="300"
        src="https://www.youtube.com/embed/NmSEJq4Mfk0"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
</iframe>

Dans les années 1990, ARPANET devient **Internet**, un vaste ensemble de réseaux interconnectés à l’échelle planétaire. Internet repose sur le modéle **TCP/IP**, qui permet à toutes les machines du monde de parler le même langage.

Mais Internet n’est qu’une infrastructure. En 1989, **Tim Berners-Lee**, au CERN, invente le **World Wide Web**, un système qui permet de naviguer entre des documents reliés par des **liens hypertextes**. Grâce au Web et aux navigateurs comme **Mosaic**, **Netscape** ou plus tard **Chrome**, les informations deviennent accessibles à tous, en quelques clics.

Le Web transforme Internet en un **espace universel de partage, de savoir et de communication**.

Internet n’est pas une seule machine géante.  
C’est en réalité **un immense ensemble de réseaux interconnectés** :  

### LAN

Les réseaux locaux (LAN, Local Area Network)

  - Exemple : votre maison (box Internet + ordinateurs + téléphones connectés en Wi-Fi ou en câble).  
  - Exemple : le réseau du lycée (salles informatiques, imprimantes, serveurs pédagogiques).  
  - Exemple : le réseau d’une entreprise.  

Ces réseaux sont **privés et limités dans l’espace** (on les appelle des **réseaux locaux**).

![](LAN.png)

Les principaux composants d’un LAN incluent :  
- le **switch**, qui permet de connecter plusieurs ordinateurs entre eux et de gérer le trafic interne du réseau  
- le **routeur**, qui relie le LAN à d’autres réseaux, comme Internet   
- les **câbles Ethernet** assurent une connexion filaire fiable entre les appareils  
- le **Wi-Fi** permet aux appareils sans fil de se connecter au réseau  

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

Résultat :  
Quand vous envoyez un message, il sort d’abord de votre réseau local → passe par le réseau de votre FAI → traverse plusieurs autres réseaux → atteint le réseau du destinataire.  


**Idée clé à retenir :**  
Internet, c’est **l’interconnexion de milliers de réseaux locaux et de fournisseurs d’accès** à l’échelle mondiale, qui communiquent tous grâce à des **protocoles communs**.

### Conclusion

En quelques siècles, l’humanité est passée des signaux de fumée aux flux d’informations mondiaux.  
Chaque invention a rapproché les hommes, accéléré les échanges et repoussé les frontières de la communication.  

---

## Modèle en couches TCP/IP

La communication sur un réseau se fait grâce à des protocoles, qui sont des règles définissant comment les données sont envoyées, reçues et comprises par les machines.

Le modéle TCP/IP organise la communication en **4 couches**, chacune ayant un rôle spécifique et ses protocoles.  

Quand on envoie un message ou un fichier sur Internet, il n’est jamais envoyé en un seul bloc, mais découpé en petits morceaux appelés **paquets**.  

![Découpage](../../../Secondes/Chapitres/Internet/paquets.png)

Chaque couche y ajoute des informations spécifiques (adresse de destination, numéro du paquet, etc) avant de transmettre les données, c'est l'**encapsulation**.

À la réception, chaque couche retire son en-tête pour reconstituer les données originales c’est la **désencapsulation**.

![Modèle](../../../Secondes/Chapitres/Internet/model.png)

## Le protocole IP et l’adressage

Chaque appareil connecté à Internet doit être identifiable de manière **unique**.  
Pour cela, deux types d’adresses existent :

### Adresse MAC (adressage local)
Chaque appareil connecté à un réseau possède une **carte réseau** (ou interface réseau), qui permet d'envoyer et de recevoir des données. Chaque carte réseau possède une **adresse MAC** (Media Access Control), un identifiant unique attribué par le fabricant.

Un PC peut posséder **plusieurs cartes réseau**, par exemple une pour le câble Ethernet et une autre pour le Wi-Fi. Chaque carte a sa propre adresse MAC, ce qui signifie qu’un même ordinateur peut être identifié différemment selon le type de connexion utilisée.

L'adresse MAC est composée de **12 chiffres hexadécimaux**, souvent notés sous la forme `00:1A:2B:3C:4D:5E`. Elle permet d’identifier de manière unique chaque carte réseau sur un réseau local, un peu comme une **plaque d'immatriculation** pour une voiture.  

Contrairement à l'adresse IP, qui peut changer selon le réseau, l'adresse MAC reste **fixe et unique** pour chaque carte réseau. Les **switches** utilisent ces adresses MAC pour **diriger les données vers le bon appareil** sur le réseau local.

<span style="color:red">Exercices</span>  
```text
1. Combien d'adresses MAC possibles existe-t'il ?
2. Écrire 5 exemples d'adresses MAC différentes.
```

### Adresse IP (adressage global)

Chaque appareil connecté à un réseau possède une **adresse IP** (Internet Protocol), qui sert à l’identifier et à échanger des données avec d’autres appareils. Contrairement à l’adresse MAC, qui est **fixe et unique pour chaque carte réseau**, l’adresse IP peut **changer selon le réseau** auquel l’appareil est connecté.

#### Structure d’une adresse IP

Une adresse IP version 4 est composée de **4 nombres entre 0 et 255**, séparés par des points, par exemple `192.168.1.10`. Elle se divise en deux parties :

- La **partie réseau** : identifie le réseau auquel appartient l’appareil.
- La **partie hôte** : identifie l’appareil sur ce réseau.

Le **masque de sous-réseau** (subnet mask) sert à déterminer quelles parties de l’adresse IP correspondent au réseau et lesquelles correspondent à l’hôte. Par exemple, avec une adresse IP `192.168.1.10` et un masque `255.255.255.0` :

- Le **réseau** est `192.168.1.0`
- L’**hôte** est `10`

**La Notation CIDR** (Classless Inter-Domain Routing)  

Elle permet de représenter le réseau plus simplement. On écrit l’adresse suivie d’un **slash** et du nombre de bits utilisés pour la partie réseau.  

Par exemple :  

```
192.168.1.10/24
```
Le `/24` signifie que les 24 premiers bits de l’adresse correspondent le réseau (soit `255.255.255.0`)
et les 8 bits restants correspondent à l’hôte.

```
adresse en binaire : 11000000.10101000.00000001.00001010

masque (24 bits ici) : 11111111.11111111.11111111.00000000

donc la partie réseau est : 11000000.10101000.00000001.00000000
```
Il s'agit de l'adresse du réseau.

<span style="color:red">Exercices</span>  

**1) Combien d'adresses IP possibles existe-t'il ?**
  
**2) Écrire 5 exemples d'adresses IP différentes.**  
  
**3) Identifier le réseau et l’hôte**

Pour chaque adresse IP donnée, indique la **partie réseau** et la **partie hôte** en utilisant le masque fourni.

- Adresse : `192.168.1.25`  
   Masque : `255.255.255.0`  

- Adresse : `10.0.5.12`  
   Masque : `255.255.0.0`  

- Adresse : `172.16.7.34`  
   Masque : `255.255.255.240`  

**4) Déterminer si deux adresses sont sur le même réseau**

Indique si les adresses suivantes appartiennent **au même réseau**. Justifie ta réponse.
Si oui, donner 3 autres adresses possibles sur ce réseau.

- `192.168.1.10/24` et `192.168.1.200/24`  
- `10.1.5.7/16` et `10.2.3.10/16`  
- `172.16.5.20/28` et `172.16.5.25/28`  

**5) Conversion en binaire**

Convertis les adresses IP suivantes et leurs masques en **binaire**. Puis identifie la partie réseau et la partie hôte.

- `192.168.10.14/24`  
- `10.0.20.5/8`  
- `172.16.100.50/16`  

**6) Calculer le nombre d’hôtes**

Pour chaque réseau, calcule **le nombre maximum d’hôtes** possibles et indiquez la plage complète d’adresses.

- Réseau : `192.168.1.0/24`  
- Réseau : `10.0.0.0/16`  
- Réseau : `172.16.5.0/28`  

**7) Identifier le masque**

Pour chaque situation, propose le **masque le plus approprié** en notation CIDR pour le réseau.

- Un réseau doit contenir **50 hôtes maximum**.  
- Un réseau doit contenir **500 hôtes maximum**.  
- Un réseau doit contenir **12 hôtes maximum**.  

**8) IP et sous-réseaux**

Une entreprise possède le réseau `192.168.0.0/24`. Elle veut créer **4 sous-réseaux égaux**.  
- Quelle sera la **nouvelle notation CIDR** pour chaque sous-réseau ?  
- Donne l’**adresse réseau** de chaque sous-réseau.  
- Indique le **nombre d’hôtes possibles** dans chaque sous-réseau.

---

#### IPv6

Les adresses IP que nous avons utilisé jusque là correspondent au format IPv4. Utilisé depuis les débuts d’Internet, il ne permet pas d'avoir assez d'adresses pour palier à nos besoins actuels : avec la multiplication des ordinateurs, smartphones, objets connectés, consoles et serveurs, ce nombre est devenu insuffisant.  

Pour répondre à ce problème, une nouvelle version du protocole Internet a été créée : **IPv6**.

exemple d'adresse IPv6 : `2001:0db8:85a3:0000:0000:8a2e:0370:7334`

Pour simplifier, on peut **abréger** une adresse IPv6 :
- Les **zéros initiaux** d’un groupe peuvent être supprimés :  
  `2001:db8:85a3:0:0:8a2e:370:7334`
- Une suite de groupes `0000` peut être remplacée par `::` (une seule fois par adresse) :  
  `2001:db8:85a3::8a2e:370:7334`

<span style="color:red">Exercices</span>  
```text
1. Combien d'adresses IPv6 possibles existe-t'il ?
2. Écrire 5 exemples d'adresses IPv6 différentes.
```

#### DNS – Domain Name System

Quand vous tapez un nom de site dans votre navigateur, par exemple `wikipedia.org`, votre ordinateur ne sait pas directement où envoyer les paquets, il a besoin de **l’adresse IP** correspondante.
Pour éviter d'avoir à se souvenir des IPs de tous les sites, nous utilisons le DNS.  

Le **DNS (Domain Name System)** est un service qui fait la correspondance entre le Nom symbolique et l'Adresse IP par le biais de serveurs DNS.

---