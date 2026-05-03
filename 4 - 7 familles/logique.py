def trier(main):
    for i in range(len(main)):
        for j in range(len(main)):
            carte1 = main[i]
            carte2 = main[j]
            # On trie d'abord par famille
            if carte1[0] < carte2[0]:
                sauve = main[i]
                main[i] = main[j]
                main[j] = sauve
            # Si c'est la meme famille on trie par numero
            if carte1[0] == carte2[0]:
                if carte1[1] < carte2[1]:
                    sauve = main[i]
                    main[i] = main[j]
                    main[j] = sauve

def chercher(main, famille, membre):
    for i in range(len(main)):
        if main[i][0] == famille and main[i][1] == membre:
            return i
    return -1

def verif_complete(main):
    comptes = {}
    for carte in main:
        famille = carte[0]
        if famille not in comptes:
            comptes[famille] = 0
        comptes[famille] += 1
    
    for famille in comptes:
        if comptes[famille] == 6:
            return famille
    return None
