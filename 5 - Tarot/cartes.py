import random

def creer():
    p = []
    coul = ["Coeur", "Carreau", "Trefle", "Pique"]
    for c in coul:
        for v in range(1, 15):
            p.append((c, v))
    for v in range(1, 22):
        p.append(("Atout", v))
    p.append(("Excuse", 0))
    random.shuffle(p)
    return p

def distribue(p, n):
    m = []
    for i in range(n):
        if len(p) > 0:
            m.append(p.pop(0))
    return m
