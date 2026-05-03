def trier(main):
    for i in range(len(main)):
        for j in range(len(main)):
            carte1 = main[i]
            carte2 = main[j]
            # On trie par couleur
            if carte1[0] < carte2[0]:
                sauve = main[i]
                main[i] = main[j]
                main[j] = sauve
            # Si meme couleur on trie par chiffre
            if carte1[0] == carte2[0]:
                if carte1[1] < carte2[1]:
                    sauve = main[i]
                    main[i] = main[j]
                    main[j] = sauve

def peut_jouer(carte, dessus):
    if carte[0] == dessus[0] or carte[1] == dessus[1]:
        return True
    return False
