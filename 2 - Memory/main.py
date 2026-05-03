from grille import init, masque_vide, afficher
from logique import demander_coordonnees
import time

def jouer():
    grille = init()
    masque = masque_vide()
    trouves = 0
    
    while trouves < 8:
        afficher(grille, masque)
        
        print("\n[Carte 1]")
        ligne1, col1 = demander_coordonnees()
        if masque[ligne1][col1]:
            print("Cette carte est déjà révélée !")
            continue
            
        masque[ligne1][col1] = True
        afficher(grille, masque)
        
        print("\n[Carte 2]")
        ligne2, col2 = demander_coordonnees()
        if masque[ligne2][col2]:
            print("Cette carte est déjà révélée !")
            masque[ligne1][col1] = False 
            continue
            
        masque[ligne2][col2] = True
        afficher(grille, masque)
        
        if grille[ligne1][col1] == grille[ligne2][col2]:
            print("\nC'est une paire.")
            trouves += 1
        else:
            print("\nRaté !")
            time.sleep(2)
            masque[ligne1][col1] = False
            masque[ligne2][col2] = False

            print("\n" * 20)

    print("\nBien joué ! Vous avez trouvé toutes les paires.")

try: # avec IA, car quand je CTRL+C ca ne quitte pas le jeu je ne sais pas pourquoi
    jouer()
except KeyboardInterrupt:
    print("\n\nArrêt du jeu...")
