"""
Programme loup garou : fonction main
"""
"""
Variables utilisées :
liste_role : liste des personnages utilisés
liste_nom : liste des joueurs ajustés avec leur role
liste_mort : liste éphémère qui répertorie les morts pour les indiquer a la sorciere
nombre_loups : indique le nombre de loups. Est utilisé pour verifier a chaque debut de tour si la partie est finie.
"""

def main():
    liste_role = []
    liste_nom = []
    liste_mort = []
    nombre_loups = parametrage_role() #-> int la fonction parametrage_role doit demander le nombre de joueurs et parametrer les cartes en jeu.
    parametrage_nom(liste_role) #-> rien la fonction parametrage_nom affiche une boite où il faut entrer les noms des joueurs a coté des nom des cartes
    if cupidon in liste_role:
        amoureux=[]
    if sorciere in liste_role:
        potion_vie=1
        potion_mort=1
    nuit_tour1(liste_role,liste_nom): #-> str| la fontion tour1 doit executer les fonctions de personnages intervenent a la premiere nuit, modifier les listes en fonction des défunts, et ressortir un message disant qui sont les morts.
    
    

    
    
#list.sort permet de trier une liste, soir par ordre alphabetique, soit par ordre croissant
