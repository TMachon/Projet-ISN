import tkinter as tk
from tkinter import ttk
    
def parametrage_role () :
    
    def fermer_fenetre_1 () :

        fenetre_1.destroy()
    
    fenetre_1 = tk.Tk()
    fenetre_1.title("Loup-Garou : Paramétrage 1/2")
    
    #Ligne 1
    
    ####IMAGE
    
    ttk.Label(fenetre_1, text="  ").grid(row=0, column=1)
    
    ####IMAGE
    
    ttk.Label(fenetre_1, text="  ").grid(row=0, column=3)
    
    ####IMAGE
    
    ttk.Label(fenetre_1, text="  ").grid(row=0, column=5)
    
    ####IMAGE
    
    ttk.Label(fenetre_1, text="  ").grid(row=0, column=7)
    
    #Ligne 2
    
    nombre_villageois = tk.StringVar()
    combo = ttk.Combobox(fenetre_1, width=2, textvariable=nombre_villageois, state='readonly')
    combo['values'] = tuple(x for x in range(0, 14))
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
    
    ttk.Label(fenetre_1, text=" ").grid(row=2, column=0)    
    
    check_val = tk.IntVar()    
    check = ttk.Checkbutton(fenetre_1, variable=check_val, text=': Jouer avec le Capitaine ?"')
    check.grid(row=2, column=8)
    
    #Ligne 4
    
    ####IMAGES
    
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
    
    validation = ttk.Button(fenetre_1, text="Valider", command = fermer_fenetre_1)
    validation.grid(row=5, column=8)
        
    #Loop
    fenetre_1.mainloop()

    return ["1_{}_voleur".format(nombre_voleur.get()), "2_{}_cupidon".format(nombre_cupidon.get()), "3_{}_voyante".format(nombre_voyante.get()), "4_{}_loup_garou".format(nombre_loup_garou.get()), "5_{}_sorciere".format(nombre_sorciere.get()), "6_{}_petite_fille".format(nombre_petite_fille.get()), "7_{}_villageois".format(nombre_villageois.get()), "8_{}_chasseur".format(nombre_chasseur.get()), "{}_capitaine".format(check_val.get())]

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

def main () :
    liste_role = []
    liste_nom = []
    liste_temporaire = parametrage_role()
    print(liste_temporaire)
    for i in range(len(liste_temporaire)-1) :
        for j in range(int(liste_temporaire[i][2])) :
            informations = [liste_temporaire[i], j]
            role_nom = parametrage_nom (informations)
            liste_role.append(role_nom[0])
            liste_nom.append(role_nom[1])
    print(liste_nom)
    print(liste_role)
    
main ()