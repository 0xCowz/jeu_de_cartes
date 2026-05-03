from cartes import creer, divise
from logique import jouer_tour
import time

def lancer():
    print("Initialisation du deck...")
    main1, main2 = divise(creer())
    
    tour = 0
    automatique = False
    
    while main1 and main2:
        if not automatique:
            choix = input("Entrée pour jouer, 'S' pour skip : ").upper()
            if choix == "S": automatique = True

        tour += 1
        jouer_tour(main1, main2, [])
        
        if tour > 1000:
            print("Match nul (trop de tours)") # probleme de tours, le jeu ne se termine pas en dessous de 200/300..
            break

    print("\n[Fin du jeu]")
    if main1: print("Victoire de Joueur 1 !")
    elif main2: print("Victoire de Joueur 2 !")
    else: print("Égalité totale.")

lancer()
