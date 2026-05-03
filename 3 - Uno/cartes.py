import random

def creer():
    p = []
    couleurs = ["Rouge", "Bleu", "Jaune", "Vert"]
    for c in couleurs:
        for v in range(10):
            p.append((c, v))
            if v != 0:
                p.append((c, v))
    
    random.shuffle(p)
    return p

def distribue(p, n):
    m = []
    for i in range(n):
        if len(p) > 0:
            m.append(p.pop(0))
    return m
