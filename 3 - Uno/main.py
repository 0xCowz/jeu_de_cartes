from cartes import creer, distribue
from logique import peut_jouer, trier
import time
import os

# Initialise les couleurs sur Windows
os.system('')

def lancer():
    paquet = creer()
    main1 = distribue(paquet, 7) 
    main2 = distribue(paquet, 7) 
    trier(main1)
    table = paquet.pop(0)
    
    tour = 1 
    
    while len(main1) > 0 and len(main2) > 0:
        print(f"\nSur la table : {table[0]} {table[1]}")
        
        if tour == 1:
            print("\nVotre main :")
            for i in range(len(main1)):
                if peut_jouer(main1[i], table):
                    print(f"\033[92m{i}: {main1[i][0]} {main1[i][1]}\033[0m")
                else:
                    print(f"{i}: {main1[i][0]} {main1[i][1]}")
            
            choix = input("\nNuméro de la carte (ou 'P' pour piocher) : ").upper()
            
            if choix == "P":
                if len(paquet) == 0: paquet = creer()
                main1.append(paquet.pop(0))
                trier(main1)
                print("Vous avez pioché.")
                tour = 2
            else:
                try:
                    index = int(choix)
                    if peut_jouer(main1[index], table):
                        table = main1.pop(index)
                        tour = 2
                    else:
                        print("Vous ne pouvez pas jouer cette carte !")
                except (ValueError, IndexError):
                    print("Choix invalide.")
        else:
            print("\nTour du bot.")
            time.sleep(1)
            joue = False
            for i in range(len(main2)):
                if peut_jouer(main2[i], table):
                    table = main2.pop(i)
                    print(f"Le bot a joué {table[0]} {table[1]}")
                    joue = True
                    break
            
            if not joue:
                print("Le bot pioche.")
                if len(paquet) == 0: paquet = creer()
                main2.append(paquet.pop(0))
            
            tour = 1

    if len(main1) == 0:
        print("\nBien joué ! Vous avez gagné.")
    else:
        print("\nLe bot a gagné.")

try:
    lancer()
except KeyboardInterrupt:
    print("\n\nArrêt du jeu..")
