from cartes import creer, distribue
from logique import nommer, vainqueur, trier
import time
import os

os.system('')

def lancer():
    paquet = creer()
    main1 = distribue(paquet, 18)
    main2 = distribue(paquet, 18)
    trier(main1)
    
    score1 = 0
    score2 = 0
    
    while len(main1) > 0:
        print(f"\nScore: Moi {score1} | Bot {score2}")
        print("Votre main :")
        for i in range(len(main1)):
            print(f"{i}: {nommer(main1[i])}")
            
        try:
            texte = input("\nNombre de la carte : ")
            index = int(texte)
            carte1 = main1.pop(index)
        except:
            print("Invalide !")
            continue
            
        index_bot = -1
        for i in range(len(main2)):
            if main2[i][0] == carte1[0]:
                index_bot = i
                break
        
        if index_bot == -1 and carte1[0] != "Excuse":
            for i in range(len(main2)):
                if main2[i][0] == "Atout":
                    index_bot = i
                    break
        
        if index_bot == -1:
            index_bot = 0
            
        carte2 = main2.pop(index_bot)
        
        print(f"\nVous : {nommer(carte1)}")
        print(f"Bot  : {nommer(carte2)}")
        
        if vainqueur(carte1, carte2):
            print("Vous gagnez")
            score1 += 1
        else:
            print("Le bot gagne")
            score2 += 1
        
        time.sleep(1)

    print(f"\nFin - Score final : {score1} - {score2}")

try:
    lancer()
except KeyboardInterrupt:
    print("\nArrêt..")
