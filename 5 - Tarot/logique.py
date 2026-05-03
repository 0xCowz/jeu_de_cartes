def trier(main):
    for i in range(len(main)):
        for j in range(len(main)):
            carte1 = main[i]
            carte2 = main[j]
            if carte1[0] < carte2[0]:
                sauve = main[i]
                main[i] = main[j]
                main[j] = sauve
            if carte1[0] == carte2[0]:
                if carte1[1] < carte2[1]:
                    sauve = main[i]
                    main[i] = main[j]
                    main[j] = sauve

def nommer(carte):
    if carte[0] == "Excuse": return "L'Excuse"
    if carte[0] == "Atout": return f"Atout {carte[1]}"
    valeur = carte[1]
    if valeur == 11: nom = "Valet"
    elif valeur == 12: nom = "Cavalier"
    elif valeur == 13: nom = "Dame"
    elif valeur == 14: nom = "Roi"
    else: nom = str(valeur)
    return f"{nom} de {carte[0]}"

def vainqueur(carte1, carte2):
    if carte1[0] == "Excuse": return False
    if carte2[0] == "Excuse": return True
    
    if carte1[0] == "Atout" and carte2[0] != "Atout": return True
    if carte1[0] != "Atout" and carte2[0] == "Atout": return False
    
    if carte1[0] == carte2[0]:
        return carte1[1] > carte2[1]
    
    return True
