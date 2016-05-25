import tkinter as tk
from tkinter import ttk

##### -> Fonctions de paramétrage
 
def parametrage_global () :
    
    liste_role = []
    liste_nom = []
    liste_temporaire = parametrage_role()
    
    for i in range(len(liste_temporaire)) :
        for j in range(int(liste_temporaire[i][2])) :
            informations = [liste_temporaire[i], j]
            role_nom = parametrage_nom (informations)
            liste_role.append(role_nom[0])
            liste_nom.append(role_nom[1])
    
    return [liste_role, liste_nom]
 
def parametrage_role () :
    
    def fermer_fenetre_1 () :

        fenetre_1.destroy()
    
    fenetre_1 = tk.Tk()
    fenetre_1.title("Loup-Garou : Paramétrage 1/2")
    
    #Ligne 1
    
    ttk.Label(fenetre_1, text="Villageois :").grid(row=0, column=0)
    
    ttk.Label(fenetre_1, text="  ").grid(row=0, column=1)
    
    ttk.Label(fenetre_1, text="Loup-garous :").grid(row=0, column=2)
    
    ttk.Label(fenetre_1, text="  ").grid(row=0, column=3)
    
    ttk.Label(fenetre_1, text="Voyante :").grid(row=0, column=4)
    
    ttk.Label(fenetre_1, text="  ").grid(row=0, column=5)
    
    ttk.Label(fenetre_1, text="Chasseur :").grid(row=0, column=6)
    
    ttk.Label(fenetre_1, text="  ").grid(row=0, column=7)
    
    #Ligne 2
    
    nombre_villageois = tk.StringVar()
    combo = ttk.Combobox(fenetre_1, width=2, textvariable=nombre_villageois, state='readonly')
    combo['values'] = tuple(x for x in range(0, 9))
    combo.current(0)
    combo.grid(row=1, column=0)
    
    nombre_loup_garou = tk.StringVar()
    combo = ttk.Combobox(fenetre_1, width=2, textvariable=nombre_loup_garou, state='readonly')
    combo['values'] = tuple(x for x in range(2, 5))
    combo.current(0)
    combo.grid(row=1, column=2)        
    
    nombre_voyante = tk.StringVar()
    combo = ttk.Combobox(fenetre_1, width=2, textvariable=nombre_voyante, state='readonly')
    combo['values'] = tuple(x for x in range(0, 2))
    combo.current(0)
    combo.grid(row=1, column=4)
    
    nombre_chasseur = tk.StringVar()
    combo = ttk.Combobox(fenetre_1, width=2, textvariable=nombre_chasseur, state='readonly')
    combo['values'] = tuple(x for x in range(0, 2))
    combo.current(0)
    combo.grid(row=1, column=6)
    
    #Ligne 3
    
    validation = ttk.Button(fenetre_1, text="Valider", command = fermer_fenetre_1)
    validation.grid(row=2, column=8) 
    
    #Ligne 4
    
    ttk.Label(fenetre_1, text="Cupidon :").grid(row=3, column=0)
    
    ttk.Label(fenetre_1, text="  ").grid(row=3, column=1)
    
    ttk.Label(fenetre_1, text="Socière :").grid(row=3, column=2)
    
    ttk.Label(fenetre_1, text="  ").grid(row=3, column=3)
    
    ttk.Label(fenetre_1, text="Petite fille :").grid(row=3, column=4)
    
    ttk.Label(fenetre_1, text="  ").grid(row=3, column=5)
    
    ttk.Label(fenetre_1, text="Voleur :").grid(row=3, column=6)
    
    ttk.Label(fenetre_1, text="  ").grid(row=3, column=7)
    
    #Ligne 5
    
    nombre_cupidon = tk.StringVar()
    combo = ttk.Combobox(fenetre_1, width=2, textvariable=nombre_cupidon, state='readonly')
    combo['values'] = tuple(x for x in range(0, 2))
    combo.current(0)
    combo.grid(row=4, column=0)
    
    nombre_sorciere = tk.StringVar()
    combo = ttk.Combobox(fenetre_1, width=2, textvariable=nombre_sorciere, state='readonly')
    combo['values'] = tuple(x for x in range(0, 2))
    combo.current(0)
    combo.grid(row=4, column=2)        
    
    nombre_petite_fille = tk.StringVar()
    combo = ttk.Combobox(fenetre_1, width=2, textvariable=nombre_petite_fille, state='readonly')
    combo['values'] = tuple(x for x in range(0, 2))
    combo.current(0)
    combo.grid(row=4, column=4)
    
    nombre_voleur = tk.StringVar()
    combo = ttk.Combobox(fenetre_1, width=2, textvariable=nombre_voleur, state='readonly')
    combo['values'] = tuple(x for x in range(0, 2))
    combo.current(0)
    combo.grid(row=4, column=6)
        
    #Loop
        
    fenetre_1.mainloop()

    return ["1_{}_voleur".format(nombre_voleur.get()), "2_{}_cupidon".format(nombre_cupidon.get()), "3_{}_voyante".format(nombre_voyante.get()), "4_{}_loup_garou".format(nombre_loup_garou.get()), "5_{}_sorciere".format(nombre_sorciere.get()), "6_{}_petite_fille".format(nombre_petite_fille.get()), "7_{}_villageois".format(nombre_villageois.get()), "8_{}_chasseur".format(nombre_chasseur.get())]

def parametrage_nom (informations) :
    
    def fermer_fenetre_2 () :

        fenetre_2.destroy()
    
    if informations[0][4:] == 'cupidon' :
        prefixe = 'de '
    elif informations[0][4:] == 'voyante' :
        prefixe = 'de la '
    elif informations[0][4:] == 'sorciere' :
        prefixe = 'de la '
    elif informations[0][4:] == 'petite_fille' :
        prefixe = 'de la '
    else :
        prefixe = 'du '
        
    debut_texte = prefixe + informations[0][4:].replace('_',' ')
    
    if informations[0][0] == '4' :
        fin_texte = ' n°{} '.format(str(informations[1]+1))
    elif informations[0][0] == '7' :
        fin_texte = ' n°{} '.format(str(informations[1]+1))
    else :
        fin_texte = ' '
    
    fenetre_2 = tk.Tk()
    fenetre_2.title("Loup-Garou : Paramétrage 2/2")
    
    #Ligne 1

    ttk.Label(fenetre_2, text="Quel est le nom {}{}?".format(debut_texte, fin_texte)).grid(row=0, column=0)

    #Ligne 2
    
    prenom = tk.StringVar()
    ttk.Entry(fenetre_2, width=10, textvariable=prenom).grid(row=1, column=0)
    
    validation = ttk.Button(fenetre_2, text="Valider", command = fermer_fenetre_2)
    validation.grid(row=5, column=8)
    
    #Loop
    
    fenetre_2.mainloop()
    
    role = '{}_{}_{}'.format(informations[0][0], str(informations[1]), informations[0][4:])
    nom = '{}_{}'.format(role[0:3], prenom.get())
    
    return [role, nom]    

##### -> Fonctions des nuits

def tours (liste_role_nom) :
    
    fin = 0
    tour_cupidon = 0
    amoureux = ["0", "0"]
    potions_sorciere = [0, 0]
    deces_amoureux = 0
    deces_chasseur = 0
    
    #NUIT
    
    while fin != 1 :
        
        morts = []
        
        nombre_loup_garous = 0
        for i in range(len(liste_role_nom[0])) :
            if liste_role_nom[0][i][0] == '4' :
                nombre_loup_garous += 1
            
        if nombre_loup_garous == len(liste_role_nom[0]):
            fin_loup_garous()
            break
        elif nombre_loup_garous == 0 :
            fin_villageois()
            break
        else :
            if '1_0_voleur' in liste_role_nom[0] :
                liste_role_nom = voleur(liste_role_nom)
                
            if ('2_0_cupidon' in liste_role_nom[0]) and (tour_cupidon == 0) :
                while amoureux[1] == amoureux [0] :
                    amoureux = cupidon(liste_role_nom)
                tour_cupidon += 1
              
            if '3_0_voyante' in liste_role_nom[0] :
                voyante()
    
            mort_loup_garou = loup_garou(liste_role_nom)
            morts.append(mort_loup_garou)
        
            if '5_0_sorciere' in liste_role_nom[0] :
                if (potions_sorciere[0] == 0) or (potions_sorciere[1] == 0) :
                    changements = sorciere(liste_role_nom, morts, potions_sorciere)
                    if changements[0] == 1 :
                        morts.remove(morts[0])
                    if changements[1] != 'Personne' :
                        morts.append(changements[0])
                    potions_sorciere = changements[2]
                    
    #JOUR
            
            for i in range(2) :
                if deces_amoureux == 0 :
                    if amoureux != ["0", "0"] :
                        mort_amoureux = test_amoureux(amoureux, morts)
                        if mort_amoureux != 0 :
                            morts.append(mort_amoureux)
                            deces_amoureux += 1
                if deces_chasseur == 0 :
                    for y in range(len(morts)) :
                        if morts[y][:4] == '8_0_' :
                            mort_chasseur = chasseur(liste_role_nom)
                            morts.append(mort_chasseur)
                            deces_chasseur +=1
            
            liste_role_nom = triage_morts(liste_role_nom, morts)
            annonce_morts(morts)
            morts = []
            
            nombre_loup_garous = 0
            for i in range(len(liste_role_nom[0])) :
                if liste_role_nom[0][i][0] == '4' :
                    nombre_loup_garous += 1
            
            if nombre_loup_garous == len(liste_role_nom[0]):
                fin_loup_garous()
                break
            elif nombre_loup_garous == 0 :
                fin_villageois()
                break
            else :
                mort_villageois = village(liste_role_nom)
                morts.append(mort_villageois)
                
                for i in range(2) :
                    if deces_amoureux == 0 :
                        if amoureux != ["0", "0"] :
                            mort_amoureux = test_amoureux(amoureux, morts)
                            if mort_amoureux != 0 :
                                morts.append(mort_amoureux)
                                deces_amoureux += 1
                    if deces_chasseur == 0 :
                        for y in range(len(morts)) :
                            if morts[y][:4] == '8_0_' :
                                mort_chasseur = chasseur(liste_role_nom)
                                morts.append(mort_chasseur)
                                deces_chasseur +=1
                            
                liste_role_nom = triage_morts(liste_role_nom, morts)
                morts = []
            
            nombre_loup_garous = 0
            for i in range(len(liste_role_nom[0])) :
                if liste_role_nom[0][i][0] == '4' :
                    nombre_loup_garous += 1            
            
            if nombre_loup_garous == len(liste_role_nom[0]):
                fin_loup_garous()
                break
            elif nombre_loup_garous == 0 :
                fin_villageois()    
                break
 
def triage_morts (liste_role_nom, morts) :
    
    indices_morts = []
    for i in range(len(liste_role_nom[0])) :
        for y in range(len(morts)) :
            if liste_role_nom[0][i][:4] == morts[y][:4] :
                indices_morts.append(i)
    for i in range(len(indices_morts)) :
        liste_role_nom[0].remove(liste_role_nom[0][indices_morts[i]])
        liste_role_nom[1].remove(liste_role_nom[1][indices_morts[i]])
        
    return liste_role_nom

def test_amoureux (amoureux, morts) :
    
    nombre_amoureux_morts = 0
    for i in range(len(amoureux)) :
        for y in range(len(morts)) :
            if amoureux[i] == morts[y] :
                nombre_amoureux_morts += 1
                mort_amoureux = amoureux[i-1]
    
    if nombre_amoureux_morts != 1:
        mort_amoureux = 0
    
    return mort_amoureux
    
def annonce_morts (morts) :
    
    def fermer_fenetre_annonce () :

        fenetre_annonce.destroy()
    
    if len(morts) > 0 :
        annonce = 'Sont morts cette nuit : {}'.format(morts[0][4:])
    if len(morts) > 1 :
        for i in range(len(morts)-1) :
            annonce += " {}" .format(morts[i+1][4:])
    
    fenetre_annonce = tk.Tk()
    fenetre_annonce.title("Les morts de la nuit")
        
    #Ligne 1
    
    ttk.Label(fenetre_annonce, text=annonce).grid(row=0, column=0)
    
    #Ligne 2
    
    validation = ttk.Button(fenetre_annonce, text="Valider", command = fermer_fenetre_annonce)
    validation.grid(row=1, column=0)
    
    #Loop

    fenetre_annonce.mainloop()

def fin_loup_garous () :
    
    fenetre_loup_garou = tk.Tk()
    fenetre_loup_garou.title("Victoire des loup-garous !")
    
    #Ligne 1
    
    ttk.Label(fenetre_loup_garou, text="Les loup-garous ont gagnés !").grid(row=0, column=0)
    
    #Ligne 2
    
    validation = ttk.Button(fenetre_loup_garou, text="Valider", command = fin)
    validation.grid(row=1, column=0)
    
    #Loop

    fenetre_loup_garou.mainloop()

def fin_villageois () :
    
    fenetre_villageois = tk.Tk()
    fenetre_villageois.title("Victoire des villageois !")
    
    #Ligne 1
    
    ttk.Label(fenetre_villageois, text="Les villageois ont gagnés !").grid(row=0, column=0)
    
    #Ligne 2
    
    validation = ttk.Button(fenetre_villageois, text="Valider", command = fin)
    validation.grid(row=1, column=0)
    
    #Loop

    fenetre_villageois.mainloop()

##### -> Fonctions des rôles
    
def voleur (liste_role_nom) :
    
    def fermer_fenetre_voleur () :

        fenetre_voleur.destroy()    
                
    affichage = ['Cupidon', 'Voyante', 'Loup garou', 'Sorciere', 'Petite fille', 'Villageois', 'Chasseur']
    
    fenetre_voleur = tk.Tk()
    fenetre_voleur.title("Loup-Garou : Voleur")
    
    #Ligne 1
    
    ttk.Label(fenetre_voleur, text="Quelle est la nouvelle carte choisie par le voleur ?").grid(row=0, column=0)
    
    #Ligne 2
    
    reponse = tk.StringVar()
    combo = ttk.Combobox(fenetre_voleur, width=10, textvariable=reponse, state='readonly')
    combo['values'] = tuple(affichage)
    combo.current(0)
    combo.grid(row=1, column=0)
    
    validation = ttk.Button(fenetre_voleur, text="Valider", command = fermer_fenetre_voleur)
    validation.grid(row=1, column=1)
    
    #Loop
    
    fenetre_voleur.mainloop()
    
    nouvelle_carte_voleur = reponse.get()
    
    cartes_dispo = ["2_0_cupidon", "3_0_voyante", "4_5_loup_garou", "5_0_sorciere", "6_0_petite_fille", "7_9_villageois", "8_0_chasseur"]
    
    for i in range(len(affichage)) :
        if nouvelle_carte_voleur == affichage[i] :
            nouveau_role = cartes_dispo[i]
        
    liste_role_nom[0].remove(liste_role_nom[0][0])
    liste_role_nom[0].append(nouveau_role)
    nouveau_nom = nouveau_role[0:4] + liste_role_nom[1][0][4:]
    liste_role_nom[1].remove(liste_role_nom[1][0])
    liste_role_nom[1].append(nouveau_nom)
    liste_role_nom[0].sort()
    liste_role_nom[1].sort()
    
    return liste_role_nom

def cupidon (liste_role_nom) :

    def fermer_fenetre_cupidon () :

        fenetre_cupidon.destroy()

    liste_pretendants = []
    for i in range(len(liste_role_nom[1])) :
        liste_pretendants.append((liste_role_nom[1][i][4].upper() + liste_role_nom[1][i][5:] + " (" + liste_role_nom[0][i][4].upper() + liste_role_nom[0][i][5:] + ")").replace('_',' '))

    fenetre_cupidon = tk.Tk()
    fenetre_cupidon.title("Loup-Garou : Cupidon")
    
    #Ligne 1
    
    ttk.Label(fenetre_cupidon, text="Qui sont les amoureux ?").grid(row=0, column=0)
        
    #Ligne 2
    
    reponse1 = tk.StringVar()
    combo = ttk.Combobox(fenetre_cupidon, width=20, textvariable=reponse1, state='readonly')
    combo['values'] = tuple(liste_pretendants)
    combo.current(0)
    combo.grid(row=1, column=0)
    
    reponse2 = tk.StringVar()
    combo = ttk.Combobox(fenetre_cupidon, width=20, textvariable=reponse2, state='readonly')
    combo['values'] = tuple(liste_pretendants)
    combo.current(0)
    combo.grid(row=1, column=1)
    
    validation = ttk.Button(fenetre_cupidon, text="Valider", command = fermer_fenetre_cupidon)
    validation.grid(row=1, column=2)
    
    #Loop
    
    fenetre_cupidon.mainloop()
    
    amoureux1 = reponse1.get()
    amoureux2 = reponse2.get()
    
    for i in range(len(liste_pretendants)) :
        if amoureux1 == liste_pretendants[i] :
            amoureux_1 = liste_role_nom[1][i]
    
    for i in range(len(liste_pretendants)) :
        if amoureux2 == liste_pretendants[i] :
            amoureux_2 = liste_role_nom[1][i]
    
    return [amoureux_1, amoureux_2]

def voyante () :

    def fermer_fenetre_voyante () :

        fenetre_voyante.destroy()

    fenetre_voyante = tk.Tk()
    fenetre_voyante.title("Loup-Garou : Voyante")
    
    #Ligne 1
    
    ttk.Label(fenetre_voyante, text="La voyante se réveille.").grid(row=0, column=0) 
    
    #Ligne 2
    
    validation = ttk.Button(fenetre_voyante, text="Valider", command = fermer_fenetre_voyante)
    validation.grid(row=1, column=2)
    
def loup_garou (liste_role_nom) :
    
    def fermer_fenetre_loup_garou () :
        
        fenetre_loup_garou.destroy()
     
    affichage = []
    for i in range(len(liste_role_nom[1])) :
        affichage.append((liste_role_nom[1][i][4].upper() + liste_role_nom[1][i][5:] + " (" + liste_role_nom[0][i][4].upper() + liste_role_nom[0][i][5:] + ")").replace('_',' '))

     
    fenetre_loup_garou = tk.Tk()
    fenetre_loup_garou.title("Loup-Garou : Loup-garous")
    
    #Ligne 1
    
    ttk.Label(fenetre_loup_garou, text="Quelle est la victime des loup-garous ?").grid(row=0, column=0)
        
    #Ligne 2
    
    reponse = tk.StringVar()
    combo = ttk.Combobox(fenetre_loup_garou, width=20, textvariable=reponse, state='readonly')
    combo['values'] = tuple(affichage)
    combo.current(0)
    combo.grid(row=1, column=0)
    
    validation = ttk.Button(fenetre_loup_garou, text="Valider", command = fermer_fenetre_loup_garou)
    validation.grid(row=1, column=2)
    
    #Loop
    
    fenetre_loup_garou.mainloop()
    
    mort_loup_garou = reponse.get()
    
    for i in range(len(affichage)) :
        if mort_loup_garou == affichage[i] :
            mort_loup_garou = liste_role_nom[1][i]
            
    return mort_loup_garou

def sorciere (liste_role_nom, morts, potions_sorciere) :
    
    def fermer_fenetre_sorciere () :
        
        fenetre_sorciere.destroy()    
    
    affichage = []
    for i in range(len(liste_role_nom[1])) :
        affichage.append(liste_role_nom[1][i][4].upper() + liste_role_nom[1][i][5:] + " (" + liste_role_nom[0][i][4].upper() + liste_role_nom[0][i][5:] + ")".replace('_',' '))
    affichage.append('Personne')
    
    for i in range(2) :    
        liste_role_nom[i].append('Personne')
    
    texte = "La sorcière sauve-t-elle la victime des loup-garous : {} ?".format(morts[0][4:])
    
    fenetre_sorciere = tk.Tk()
    fenetre_sorciere.title("Loup-Garou : Sorcière")
    
    #Ligne 1
    
    ttk.Label(fenetre_sorciere, text="Quelle est la victime de la sorcière ?").grid(row=0, column=0)
        
    #Ligne 2
    
    reponse = tk.StringVar()
    combo = ttk.Combobox(fenetre_sorciere, width=20, textvariable=reponse, state='readonly')
    combo['values'] = tuple(affichage)
    combo.current(0)
    combo.grid(row=1, column=0)
    
    #Ligne 3

    ttk.Label(fenetre_sorciere, text="   ").grid(row=2, column=0)

    #Ligne 4

    check_val = tk.IntVar()
    check = ttk.Checkbutton(fenetre_sorciere, variable=check_val, text=texte)
    check.grid(row=3, column=0, sticky="w")

    validation = ttk.Button(fenetre_sorciere, text="Valider", command = fermer_fenetre_sorciere)
    validation.grid(row=3, column=1)
    
    #Loop
    
    fenetre_sorciere.mainloop()
    
    mort_sorciere = reponse.get()
    
    if mort_sorciere != 'Personne' :
        potions_sorciere[0] += 1
        for i in range(len(affichage)) :
            if mort_sorciere == affichage[i] :
                mort_sorciere = liste_role_nom[1][i]
                
    if check_val == 1 :
        potions_sorciere[1] += 1
            
    return [check_val, mort_sorciere, potions_sorciere]
    
def chasseur (liste_role_nom) :
    
    def fermer_fenetre_chasseur () :
        
        fenetre_chasseur.destroy()
     
    affichage = []
    for i in range(len(liste_role_nom[1])) :
        affichage.append(liste_role_nom[1][i][4].upper() + liste_role_nom[1][i][5:] + " (" + liste_role_nom[0][i][4].upper() + liste_role_nom[0][i][5:] + ")".replace('_',' '))

    fenetre_chasseur = tk.Tk()
    fenetre_chasseur.title("Loup-Garou : Loup-garous")
    
    #Ligne 1
    
    ttk.Label(fenetre_chasseur, text="Quelle est la victime du chasseur ?").grid(row=0, column=0)
        
    #Ligne 2
    
    reponse = tk.StringVar()
    combo = ttk.Combobox(fenetre_chasseur, width=20, textvariable=reponse, state='readonly')
    combo['values'] = tuple(affichage)
    combo.current(0)
    combo.grid(row=1, column=0)
    
    validation = ttk.Button(fenetre_chasseur, text="Valider", command = fermer_fenetre_chasseur)
    validation.grid(row=1, column=2)
    
    #Loop
    
    fenetre_chasseur.mainloop()
    
    mort_chasseur = reponse.get
    
    for i in range(len(affichage)) :
        if mort_chasseur == affichage[i] :
            mort_chasseur = liste_role_nom[1][i]
            
    return mort_chasseur

def village (liste_role_nom) :
    
    def fermer_fenetre_village () :
        
        fenetre_village.destroy()
     
    affichage = []
    for i in range(len(liste_role_nom[1])) :
        affichage.append(liste_role_nom[1][i][4].upper() + liste_role_nom[1][i][5:] + " (" + liste_role_nom[0][i][4].upper() + liste_role_nom[0][i][5:] + ")".replace('_',' '))
 
    fenetre_village = tk.Tk()
    fenetre_village.title("Loup-Garou : Loup-garous")
    
    #Ligne 1
    
    ttk.Label(fenetre_village, text="Quelle est la victime du village ?").grid(row=0, column=0)
        
    #Ligne 2
    
    reponse = tk.StringVar()
    combo = ttk.Combobox(fenetre_village, width=20, textvariable=reponse, state='readonly')
    combo['values'] = tuple(affichage)
    combo.current(0)
    combo.grid(row=1, column=0)
    
    validation = ttk.Button(fenetre_village, text="Valider", command = fermer_fenetre_village)
    validation.grid(row=1, column=2)
    
    #Loop
    
    fenetre_village.mainloop()
    
    mort_village = reponse.get()
    
    for i in range(len(affichage)) :
        if mort_village == affichage[i] :
            mort_village = liste_role_nom[1][i]
    
    return mort_village
    
##### -> MAIN
   
def fin () :
    
    quit()
   
def main () :
    
    liste_role_nom = parametrage_global()
    tours(liste_role_nom)
    
main()