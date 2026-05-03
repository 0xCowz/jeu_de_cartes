from cartes import creer, distribue
from logique import chercher, verif_complete, trier
import random
import time
import os

os.system('')

def jouer():
    pioche = creer()
    main1 = distribue(pioche, 6) 
    main2 = distribue(pioche, 6) 
    trier(main1)
    
    score1 = 0
    score2 = 0
    tour = 1
    
    familles = ["Rouge", "Bleu", "Jaune", "Vert", "Orange", "Violet", "Gris"]

    while (len(main1) > 0 or len(main2) > 0) and (len(pioche) > 0 or score1 + score2 < 7):
        print(f"\nScore: : Moi {score1} | Bot {score2}")
        
        if tour == 1:
            print("\nVotre main :", main1)
            print("Familles possibles :", familles)
            
            fam_demandee = input("Quelle famille demandez-vous ? ").capitalize()
            mem_demande = input("Quel membre (1 à 6) ? ")
            
            possede_famille = False
            for carte in main1:
                if carte[0] == fam_demandee: possede_famille = True
            
            if not possede_famille:
                print("Vous devez avoir au moins une carte de cette famille !")
                continue
                
            index = chercher(main2, fam_demandee, mem_demande)
            if index != -1:
                print(f"Le bot vous donne le {mem_demande} {fam_demandee}.")
                main1.append(main2.pop(index))
                trier(main1)
            else:
                print("Pioche !")
                if len(pioche) > 0:
                    carte_piochee = pioche.pop(0)
                    main1.append(carte_piochee)
                    trier(main1)
                    if carte_piochee[0] == fam_demandee and carte_piochee[1] == mem_demande:
                        print(f"Vous avez pioché le {mem_demande} {fam_demandee}. Vous rejouez !")
                    else:
                        print(f"Vous avez pioché : {carte_piochee[0]} {carte_piochee[1]}")
                        tour = 2
                else:
                    print("La pioche est vide...")
                    tour = 2
        else:
            print("\nTour du bot..")
            time.sleep(1)
            if len(main2) == 0: tour = 1; continue
            
            carte_bot = random.choice(main2)
            fam_bot = carte_bot[0]
            mem_bot = str(random.randint(1, 6))
            
            print(f"Le bot demande le {mem_bot} {fam_bot}.")
            index = chercher(main1, fam_bot, mem_bot)
            
            if index != -1:
                print("Vous lui donnez la carte.")
                main2.append(main1.pop(index))
            else:
                print("Le bot pioche.")
                if len(pioche) > 0:
                    carte_piochee = pioche.pop(0)
                    main2.append(carte_piochee)
                    if carte_piochee[0] == fam_bot and carte_piochee[1] == mem_bot:
                        print("Il a pioché la bonne carte et continue !")
                    else:
                        tour = 1
                else:
                    tour = 1

        for main_joueur, score_key in [(main1, '1'), (main2, '2')]:
            fam_complete = verif_complete(main_joueur)
            if fam_complete:
                print(f"Famille {fam_complete.upper()} complète !")
                nouvelle_main = []
                for carte in main_joueur:
                    if carte[0] != fam_complete:
                        nouvelle_main.append(carte)
                
                if score_key == '1':
                    main1 = nouvelle_main
                    score1 += 1
                else:
                    main2 = nouvelle_main
                    score2 += 1

    print(f"\nPartie finie.")
    print(f"Score final : Vous {score1} | Bot {score2}")

try:
    jouer()
except KeyboardInterrupt:
    print("\n\nArrêt du jeu..")
