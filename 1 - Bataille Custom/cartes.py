import random

def creer():
    # On passe à un deck de 32 cartes pour des parties plus courtes
    # (Cartes de 7 à 14)
    toutes = []
    for v in range(7, 15):
        toutes.append(v)
        toutes.append(v)
        toutes.append(v)
        toutes.append(v)
    
    random.shuffle(toutes)
    return toutes

def divise(paquet):
    # 16 cartes chacun (32 au total)
    p1 = []
    p2 = []
    for i in range(32):
        if i < 16:
            p1.append(paquet[i])
        else:
            p2.append(paquet[i])
    return p1, p2
