import random

def nommer(v):
    if v == 11: return "Valet"
    if v == 12: return "Dame"
    if v == 13: return "Roi"
    if v == 14: return "As"
    return str(v)

def jouer_tour(main1, main2, pot):
    if len(main1) == 0 or len(main2) == 0: 
        return
    
    carte1 = main1.pop(0)
    carte2 = main2.pop(0)
    pot.append(carte1)
    pot.append(carte2)
    
    nom1 = nommer(carte1)
    nom2 = nommer(carte2)
    
    print(f"Joueur 1 a jouer la carte {nom1} et joueur 2 a jouer la carte {nom2}")
    
    if carte1 > carte2:
        random.shuffle(pot)
        for carte in pot:
            main1.append(carte)
        print("Joueur 1 gagne.")
    elif carte2 > carte1:
        random.shuffle(pot)
        for carte in pot:
            main2.append(carte)
        print("Joueur 2 gagne.")
    else:
        print("BATAILLE !")
        if len(main1) > 1 and len(main2) > 1:
            pot.append(main1.pop(0))
            pot.append(main2.pop(0))
            jouer_tour(main1, main2, pot)
        else:
            if len(main1) < len(main2):
                while len(main1) > 0: main1.pop()
            else:
                while len(main2) > 0: main2.pop()
