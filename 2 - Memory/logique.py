def demander_coordonnees():
    while True:
        try:
            saisie = input("Entrez Ligne et Col (ex: 0 2) : ")
            parties = saisie.split()
            ligne = int(parties[0])
            colonne = int(parties[1])
            
            if 0 <= ligne < 4 and 0 <= colonne < 4:
                return ligne, colonne
            print("En dehors de la grille !")
        except (ValueError, IndexError):
            print("Il faut deux chiffres entre 0 et 3.")
