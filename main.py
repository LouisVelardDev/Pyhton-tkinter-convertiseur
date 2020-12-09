import tkFont

from tkinter import *

import tkinter.font as font


def B2V10():
    n = enter_du_choix1.get()
    bin_list = list(n)
    int_val = ""
    for k in bin_list:
        int_val += str(int(k))
    texte1.config(text=int(int_val, 2))


def B10V2():
    c2 = enter_du_choix2.get()
    nbf = []
    while c2 != 0:
        bi = int(c2) % 2
        c2 = int(c2) // 2
        nbf = nbf + [bi]
    texte2.config(text=nbf)


def B16V2():
    c3 = enter_du_choix3.get()
    nbd = int(c3, 16)
    nbf = []
    while nbd != 0:
        bi = nbd % 2
        nbd = nbd // 2
        nbf = nbf + [bi]
    nbf.reverse()
    texte3.config(text=nbf)


def B10V16():
    c4 = enter_du_choix4.get()
    nbf = hex(int(c4))
    texte4.config(text=nbf)


def B2V16():
    c5 = enter_du_choix5.get()
    nbf = hex(int(c5, 2))
    texte5.config(text=nbf)


def B16V10():
    c6 = enter_du_choix6.get()
    nbf = int(c6, 16)
    texte6.config(text=nbf)
def resete():
    texte1.config(text="base 2 vers base 10")
    texte2.config(text="base 10 vers base 2")
    texte3.config(text="base 16 vers base 2")
    texte4.config(text="base 10 vers base 16")
    texte5.config(text="base 2 vers base 16")
    texte6.config(text="base 16 vers base 10")

root = Tk()

root.title(' convertiseur de base ')

root.minsize(1920, 1080)

enter_du_choix1 = Entry(root)


enter_du_choix2 = Entry(root)


enter_du_choix3 = Entry(root)


enter_du_choix4 = Entry(root)


enter_du_choix5 = Entry(root)


enter_du_choix6 = Entry(root)


Bouton1 = Button(root, text="convertir", command=B2V10)
Bouton2 = Button(root, text="convertir", command=B10V2)
Bouton3 = Button(root, text="convertir", command=B16V2)
Bouton4 = Button(root, text="convertir", command=B10V16)
Bouton5 = Button(root, text="convertir", command=B2V16)
Bouton6 = Button(root, text="convertir", command=B16V10)
BoutonR = Button(root, text="reset", command=resete,height = 5,width = 20)

fontStyle = tkFont.Font(family="Lucida Grande", size=45)

fontStyle2 = tkFont.Font(family="Lucida Grande", size=27)

texte_bienvenue = Label(root, text='bienvenue dans le convertiseur de base ', anchor='center', font=fontStyle)

texte1 = Label(root, text="base 2 vers base 10", anchor='center', font=fontStyle2)
texte2 = Label(root, text="base 10 vers base 2", anchor='center', font=fontStyle2)
texte3 = Label(root, text="base 16 vers base 2", anchor='center', font=fontStyle2)
texte4 = Label(root, text="base 10 vers base 16", anchor='center', font=fontStyle2)
texte5 = Label(root, text="base 2 vers base 16", anchor='center', font=fontStyle2)
texte6 = Label(root, text="base 16 vers base 10", anchor='center', font=fontStyle2)


texte_bienvenue.pack()

texte1.pack()
enter_du_choix1.pack()
Bouton1.pack()

texte2.pack()
enter_du_choix2.pack()
Bouton2.pack()

texte3.pack()
enter_du_choix3.pack()
Bouton3.pack()

texte4.pack()
enter_du_choix4.pack()
Bouton4.pack()

texte5.pack()
enter_du_choix5.pack()
Bouton5.pack()

texte6.pack()
enter_du_choix6.pack()
Bouton6.pack()

BoutonR.pack()


root.mainloop()
