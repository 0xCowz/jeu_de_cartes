import random

def init():
    valeurs = []
    for i in range(1, 9):
        valeurs.append(i)
        valeurs.append(i)
    
    random.shuffle(valeurs)
    
    g = []
    for i in range(4):
        ligne = []
        for j in range(4):
            ligne.append(valeurs[i*4 + j])
        g.append(ligne)
    return g

def masque_vide():
    m = []
    for i in range(4):
        l = []
        for j in range(4):
            l.append(False)
        m.append(l)
    return m

def afficher(g, m):
    print("\n    0 1 2 3")
    print("  ---------")
    for i in range(4):
        print(f"{i} |", end=" ")
        for j in range(4):
            if m[i][j]:
                print(g[i][j], end=" ")
            else:
                print("?", end=" ") # pas decouvert
        print()
