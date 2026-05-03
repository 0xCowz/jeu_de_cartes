# Une collection de jeux de cartes.

---

## Sommaire

1. [Liste des jeux disponibles](#-liste-des-jeux-disponibles)
2. [Comment ça a été conçu ?](#-comment-ça-a-été-conçu-)

---

## Liste des jeux disponibles

### 1. Bataille 
- **Nombre de joueurs** : 1 Joueur vs Ordinateur.
- **Objectif** : Remporter toutes les cartes du paquet en ayant la carte la plus forte à chaque tour.
- **Le petit plus** : Des couleurs dans la console pour mieux s'y retrouver !

### 2. Memory
- **Nombre de joueurs** : 1 Joueur.
- **Objectif** : Retrouver toutes les paires de cartes cachées dans la grille en un minimum de coups.
- **Le petit plus** : Une grille interactive qui se met à jour en temps réel.

### 3. Uno
- **Nombre de joueurs** : 1 Joueur vs 3 Ordinateurs.
- **Objectif** : Être le premier à se débarrasser de toutes ses cartes en respectant les couleurs ou les chiffres.
- **Le petit plus** : Gestion complète des cartes spéciales (+2, inversion, changement de couleur).

### 4. 7 Familles
- **Nombre de joueurs** : 1 Joueur vs 3 Ordinateurs.
- **Objectif** : Réunir le plus grand nombre de familles complètes (6 cartes par famille).
- **Le petit plus** : Une IA qui se souvient (un peu) de ce que vous demandez !

### 5. Tarot (Simplifié)
- **Nombre de joueurs** : 1 Joueur vs 3 Ordinateurs.
- **Objectif** : Marquer le plus de points possible grâce aux plis et aux "Bouts" (Petit, 21, Excuse).
- **Le petit plus** : Une version allégée pour apprendre les bases du Tarot sans se prendre la tête.

---

## Comment ça a été conçu ?

1. **Fichiers** : Chaque jeu est divisé en plusieurs fichiers :
   - `main.py` : Le main, qui gère le déroulement du jeu.
   - `logique.py` : Le "cerveau" qui contient les règles (qui gagne ? quelle carte peut être jouée ? les functions en globalité).
   - `cartes.py` / `grille.py` : Les données (création du paquet, mélange, etc.).
2. **Stabilité** : Gestion des erreurs pour ne pas faire crash les jeux.
