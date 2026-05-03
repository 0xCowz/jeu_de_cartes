import random

def creer():
    fams = ["Rouge", "Bleu", "Jaune", "Vert", "Orange", "Violet", "Gris"]
    membs = ["1", "2", "3", "4", "5", "6"]
    
    p = []
    for f in fams:
        for m in membs:
            p.append((f, m))
            
    random.shuffle(p)
    return p

def distribue(p, n):
    m = []
    for i in range(n):
        if len(p) > 0:
            m.append(p.pop(0))
    return m
