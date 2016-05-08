import tkinter as tk
from tkinter import ttk
    
def Parametrage_fentre_1 () :
    
    def Fermer_fenetre_1 () :

        fenetre_1.destroy()
    
    fenetre_1 = tk.Tk()
    fenetre_1.title("Loup-Garou : Paramétrage 1/2")
    
    #Ligne 1
    ttk.Label(fenetre_1, text="Nombre de joueurs : ").grid(row=0, column=0)
    
    ttk.Label(fenetre_1, text="                    ").grid(row=0, column=1)
    
    check_val1 = tk.IntVar()
    check1 = ttk.Checkbutton(fenetre_1, variable=check_val1, text=': Extension "Nouvelle Lune"')
    check1.grid(row=0, column=2, sticky="w")
    
    #Ligne 2
    joueurs = tk.StringVar()
    combo = ttk.Combobox(fenetre_1, width=10, textvariable=joueurs, state='readonly')
    combo['values'] = tuple(x for x in range(6, 31))
    combo.current(0)
    combo.grid(row=1, column=0, sticky="w")


    check_val2 = tk.IntVar()
    check2 = ttk.Checkbutton(fenetre_1, variable=check_val2, text=': Extension "Village"')
    check2.grid(row=1, column=2, sticky="w")

    
    #Ligne 3
    check_val3 = tk.IntVar()
    check3 = ttk.Checkbutton(fenetre_1, variable=check_val3, text=': Extension "Personnages"')
    check3.grid(row=2, column=2, sticky="w")
    
    #Ligne 4
    validation = ttk.Button(fenetre_1, text="Valider", command = Fermer_fenetre_1)
    validation.grid(row=3, column=0)
    validation.config(compound='left')
    
    #Loop
    fenetre_1.mainloop()

    return [check_val1.get(), check_val2.get(), check_val3.get(), int(joueurs.get())]
    
def Parametrage_fentre_2 (liste) :
    
    def Fermer_fenetre_2 () :

        fenetre_2.destroy()
        
    ext_NV = liste[0]
    ext_Vi = liste[1]
    ext_Pe = liste[2]
    
    fenetre_2 = tk.Tk()
    fenetre_2.title("Loup-Garou : Paramétrage 2/2")

def Main () :
    a=Parametrage_fentre_1()
    print(a)

Main ()