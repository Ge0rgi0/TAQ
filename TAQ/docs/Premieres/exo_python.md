# Série d’exercices sur les boucles

## 1. Boucles bornées

1. **Affichage de nombres**  
    Écrire un programme qui affiche les nombres de 1 à 10.
    Modifier le programme pour afficher uniquement les nombres pairs entre 1 et 20.

2. **Somme et produit**  
    Demander un entier `n` à l’utilisateur et afficher la somme des entiers de 1 à `n`.
    Bonus : afficher aussi le produit des entiers de 1 à `n`.

3. **Tables de multiplication**  
    Écrire un programme qui affiche la table de multiplication d’un nombre donné par l’utilisateur (exemple : table de 7).

4. **Carré d’étoiles**  
    Demander un entier `n` et afficher un carré de `n × n` étoiles.  
     Exemple pour `n=3` :  
     ```
     ***
     ***
     ***
     ```

5. **Triangle d’étoiles**  
    Même chose mais en triangle :  
     ```
     * 
     **
     ***
     ```

6. **Série de Fibonacci**  
    Afficher les `n` premiers termes de la suite de Fibonacci : 0, 1, 1, 2, 3, 5, 8…

7. **Petit jeu du dé**  
     Simuler 10 lancers d’un dé à 6 faces.
     Afficher les résultats.
     Bonus : compter combien de fois le 6 est sorti.

--- 

## 2. Boucles non bornées 

1. **Somme jusqu’à zéro**  
   L’utilisateur saisit une suite de nombres entiers.  
   La saisie s’arrête quand l’utilisateur entre `0`.  
   Le programme affiche alors la somme de tous les nombres saisis (hors le zéro final).  
 

2. **Compte à rebours**  
   Demander à l’utilisateur un nombre entier positif `n`.  
   Afficher un compte à rebours de `n` jusqu’à `0` inclus, en utilisant une boucle `while`.  


3. **Mot de passe**  
   Décider d'un mot de passe.
   Demander à le l'utilisateur.  
   Tant que le mot de passe saisi est incorrect, redemander à l’utilisateur.  
   Quand le bon mot de passe est saisi, afficher `"Accès autorisé"`.  

 
4. **Nombre mystère**  
   Le programme choisit un nombre aléatoire entre 1 et 100.  
   L’utilisateur doit le deviner en proposant des valeurs.  
   Le programme indique `"trop grand"` ou `"trop petit"` jusqu’à ce que la réponse soit trouvée.  


5. **Puissance**  
   Demander deux entiers `a` et `b`.  
   Calculer `a^b` à l’aide d’une boucle (sans utiliser `**`).  
