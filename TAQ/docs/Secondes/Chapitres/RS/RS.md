# 🌐 Les réseaux sociaux : identité numérique et modèle économique

---

## Introduction

Les réseaux sociaux sont des **plateformes en ligne** qui permettent de créer un profil, d’échanger du contenu, et de se connecter à d’autres personnes.

| Réseau | Type de contenu | Thème principal | Utilisateurs |
|:--------|:----------------|:----------------|:--------------------------:|
| **Facebook** | Textes, médias, événements | Vie sociale, actualités, groupes | ~3 milliards |
| **YouTube** | Vidéos longues | Divertissement, musique, tutoriels | ~2,5 milliards |
| **Instagram** | Images, vidéos courtes | Vie quotidienne, art, mode | ~2 milliards |
| **TikTok** | Vidéos courtes | Divertissement, musique, tendances | ~1,5 milliard |
| **LinkedIn** | Textes, images, CV | Réseaux professionnels, emploi | ~1 milliard |
| **Snapchat** | Photos et vidéos éphémères | Vie quotidienne, échanges rapides | ~800 millions |
| **Twitter** | Textes courts, images, liens | Actualités, opinions, politique | ~600 millions |
| **Discord** | Messages, salons vocaux | Jeux, forums de discussion | ~500 millions |
| **Pinterest** | Images, Art | Création, design, décoration | ~450 millions |
| **Reddit** | Textes, liens, images | Forums, échanges d’opinions | ~400 millions |
| **Strava** | Données sportives, images | Activités physiques, défis | ~100 millions |
| **BeReal** | Photos authentiques (1/jour) | Vie quotidienne, spontanéité | ~40 millions |

---

## Identification et authentification

### Définitions

**Identification :**  Action de se faire connaître auprès d’un service
  Exemple : Entrer son nom d’utilisateur ou son adresse mail

**Authentification :** Action de prouver que l’on est bien la personne déclaré
  Exemple : Entrer son mot de passe, un code reçu par SMS, ou utiliser une empreinte digitale

### Pourquoi s’authentifier ? 
L’authentification permet :  
- de protéger l’accès à ses données personnelles ;  
- d’éviter l’usurpation d’identité ;  
- de sécuriser les transactions (achats, démarches administratives, messageries, etc.).

### Les principaux moyens d’authentification

#### Mot de passe  
Méthode la plus courante.  
Simple à mettre en place, mais facile à pirater si faible ou réutilisée.

#### Double authentification (2FA)

La double authentification (2FA) combine **deux éléments différents** pour vérifier l’identité d’un utilisateur.  
Cela rend l’accès à un compte **beaucoup plus sûr** qu’un simple mot de passe.

**Les deux éléments principaux** :

- **Quelque chose que l’on sait** : un mot de passe, un code PIN, ou une réponse à une question secrète.  
- **Quelque chose que l’on a** : un code temporaire envoyé par SMS, généré par une application d’authentification, ou une clé de sécurité physique.

**Exemple concret**  
Pour se connecter à Facebook ou Google : après avoir entré le mot de passe, l’utilisateur doit saisir **un code reçu sur son téléphone** ou **valider avec une clé de sécurité**, ce qui empêche un pirate de se connecter même s’il connaît le mot de passe.

#### Clé de sécurité physique

Une clé de sécurité physique est un **petit appareil USB ou NFC** qui sert de “clé” numérique pour sécuriser l’accès à un compte.

**Avantages**  
- Très sûre : impossible de se connecter sans la clé, même si le mot de passe est connu.  
- Protège contre le **phishing** et les accès non autorisés.  
- Utilisée dans les **milieux professionnels** ou pour les comptes sensibles.

**Exemples d’utilisation sur les réseaux sociaux**  
- **Facebook** : activation dans les paramètres de sécurité pour sécuriser le compte.  
- **Google / YouTube** : protège Gmail et YouTube.  
- **Twitter (X)** : renforce la sécurité des comptes sensibles.  
- **LinkedIn** : option pour sécuriser les comptes professionnels.

### Les mots de passe : bonnes pratiques

#### Mauvaises habitudes courantes
- Utiliser le même mot de passe partout.  
- Choisir des mots simples : `azerty`, `123456`, `motdepasse`.  
- Réutiliser un ancien mot de passe après une fuite de données.

#### Bonnes pratiques
- Minimum 12 caractères (mieux : 16 ou plus).  
- Mélanger lettres, chiffres, majuscules, minuscules et symboles.  
- Aucune information personnelle (date de naissance, prénom, nom d’animal…).  
- Utiliser une phrase secrète facile à retenir :  
  Exemple : `MonChienMange2Croissants!`  
- Ne jamais réutiliser le même mot de passe.  
- Utiliser un gestionnaire de mots de passe (Bitwarden, KeePass, Dashlane…).  
- Activer la double authentification dès que possible.

### Vitesse de craquage des mots de passe

| Type de mot de passe | Exemple | Temps estimé pour le craquer* |
|:---------------------|:---------|:------------------------------|
| 6 lettres minuscules | `azertyq` | < 1 seconde |
| 8 caractères simples (lettres/chiffres) | `bonjour1` | quelques secondes |
| 10 caractères complexes | `M0nC0de77!` | quelques heures à jours |
| 12 caractères complexes | `S0le!lBleu2024` | plusieurs années |
| 16 caractères complexes | `MaPhraseSecr3te!42` | plusieurs millénaires |

\* Estimations selon Hive Systems (2024). Les vitesses dépendent de la puissance de calcul des ordinateurs.

<iframe width="400" height="300"
        src="https://www.youtube.com/embed/XM0jUsl_ke8"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
</iframe>

---

## L’identité numérique

L’**identité numérique** est l’**ensemble des informations** disponibles sur une personne sur Internet.

Ces informations peuvent provenir :  

- de **ce que l’on publie soi-même** (photos, messages, vidéos, commentaires) ;
- de **ce que d’autres publient à notre sujet** ;
- de **nos traces d’activité** (sites visités, likes, abonnements, historique, cookies).

> Tout ce que nous faisons en ligne laisse une **trace**.  
> Une recherche sur notre nom, un pseudonyme ou une photo peut révéler beaucoup de choses.

![Iceberg](./iceberg.png)

Notre identité numérique dépasse largement ce que nous publions volontairement. Elle se construit à partir de nos propres publications, de ce que les autres partagent sur nous, et des traces invisibles laissées automatiquement lors de nos connexions.

Tout ce que nous faisons ou laissons en ligne peut influencer notre image, même ce que nous ne voyons pas. Il est donc essentiel de réfléchir avant de publier, de gérer ses paramètres de confidentialité, et de garder à l’esprit que notre identité numérique nous échappe parfois partiellement.

### Le droit à l’oubli

Le droit à l’oubli est un droit européen prévu par le RGPD. Il permet à toute personne de demander la suppression de certaines informations la concernant sur Internet, par exemple sur les moteurs de recherche ou les sites web.

Objectif : permettre aux individus de reprendre un certain contrôle sur leur identité numérique et leur e‑réputation.

Pourquoi ce droit n’est pas suffisant ?

Même si le droit à l’oubli est puissant, il présente des limites :

- Copies et archives : des informations peuvent rester accessibles via des captures d’écran, des sites tiers ou des archives (Wayback Machine, forums, etc.).

- Hors juridiction européenne : le droit à l’oubli s’applique surtout aux entreprises et serveurs situés dans l’UE. Les contenus hors Europe peuvent rester en ligne.

- Réactivité variable : la suppression demande des démarches et peut prendre du temps, sans garantie complète.

Le droit à l’oubli aide à limiter l’exposition de certaines données, mais il ne remplace pas la prudence. Réfléchir avant de publier et bien gérer ses paramètres de confidentialité reste indispensable.

---

## E-réputation

### Définition
L’e-réputation correspond à **l’image qu’une personne, une entreprise ou une organisation renvoie sur Internet**.  
Elle se construit à partir de tout ce qui est publié ou partagé en ligne : messages, photos, commentaires, mentions, avis, etc.

### Conséquences

- Elle influence la **confiance** que les autres accordent (amis, enseignants, recruteurs).  
- Elle peut avoir un **impact professionnel** : les employeurs consultent souvent les profils publics.  
- Une mauvaise e-réputation peut être **difficile à corriger** (captures d’écran, partages, archivages).  
- Elle reflète une partie de **l’identité numérique**.

### Bonnes pratiques

- **Paramétrer la confidentialité** de ses comptes sur les réseaux sociaux.  
- **Réfléchir avant de publier** : tout contenu peut être sauvegardé ou diffusé à grande échelle.  
- **Éviter les propos insultants, discriminants ou personnels**.  
- **Rechercher régulièrement son nom** sur un moteur de recherche pour surveiller ce qui est public.  
- **Supprimer ou signaler** les contenus inappropriés ou faux.  
- **Demander le retrait** d’une information auprès d’un site (droit à l’oubli).

### Quelques outils utiles
- **Paramètres de confidentialité** sur les réseaux sociaux.  
- **Gestionnaire de mots de passe** (KeePass, Bitwarden…).  
- **Sites de nettoyage d’e-réputation** (Signal Spam, CNIL, demandes de déréférencement Google).

Avant de publier un contenu, se poser la question :  
**“Est-ce que j’accepterais que ce que je publie soit vu par un futur employeur, ma famille ou mes amis ?”**

---

## L'âge légal

La majorité numérique correspond à l’âge à partir duquel un mineur peut consentir seul au traitement de ses données personnelles sur les plateformes numériques. Cette règle protège les mineurs mais ne supprime pas les risques liés à Internet. La sensibilisation et l’accompagnement restent essentiels à tout âge.

- **Avant 15 ans :** Inscription seulement avec l’autorisation des parents. Le contrôle parental est conseillé.
- **De 15 à 17 ans :** Inscription possible de manière autonome mais l'accompagnement parental est recommandé.
- **Après 17 ans :** L'utilisateur est en autonomie complète. Il est considéré en responsabilité personnelle.

---

## Quelques sites
- [CNIL – L’identité numérique expliquée aux jeunes](https://www.cnil.fr/fr/maitriser-mon-identite-numerique)  
- [nonauharcelement.education.gouv.fr](https://www.nonauharcelement.education.gouv.fr)  
- [RGPD – Droit à l’effacement (article 17)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)

---

## Graphes

Pour cette partie, nous allons travailler sur une activité disponible sur le site : [KXS.fr](https://kxs.fr/cours/reseaux-sociaux/graphes-reseaux-sociaux).

Au programme de cette activité :
- les différentes manières de décrire / reprèsenter les liaisons entre les utilisateurs d'un réseau social
- découverte des propriètès et caractéristiques des graphes