import tkFont

from tkinter import *


def B2V10(n=int):
    nbf = int(n, 2)
    text_variable1 = nbf


def B10V2(c2):
    nbf = []
    while c2 != 0:
        bi = c2 % 2
        c2 = c2 // 2
        nbf = nbf + [bi]
    rep2 = Label(root, text=nbf, anchor='center', font=fontStyle2).pack()


def B16V2():
    nbd = int(c3, 16)
    nbf = []
    while nbd != 0:
        bi = nbd % 2
        nbd = nbd // 2
        nbf = nbf + [bi]
    nbf.reverse()
    rep3 = Label(root, text=nbf, anchor='center', font=fontStyle2).pack()


def B10V16():
    nbf = hex(int(c4))
    rep4 = Label(root, text=nbf, anchor='center', font=fontStyle2).pack()


def B2V16():
    nbf = hex(int(c5, 2))
    rep5 = Label(root, text=nbf, anchor='center', font=fontStyle2).pack()


def B16V10():
    nbf = int(c6, 16)
    rep6 = Label(root, text=nbf, anchor='center', font=fontStyle2).pack()


root = Tk()

root.title(' convertiseur de base ')

root.minsize(1920, 1080)

enter_du_choix1 = Entry(root)
n = enter_du_choix1.get()

enter_du_choix2 = Entry(root)
c2 = enter_du_choix2.get()

enter_du_choix3 = Entry(root)
c3 = enter_du_choix3.get()

enter_du_choix4 = Entry(root)
c4 = enter_du_choix4.get()

enter_du_choix5 = Entry(root)
c5 = enter_du_choix5.get()

enter_du_choix6 = Entry(root)
c6 = enter_du_choix6.get()

Bouton1 = Button(root, text="convertir", command=B2V10(n=int))
Bouton2 = Button(root, text="convertir", command=B10V2)
Bouton3 = Button(root, text="convertir", command=B16V2)
Bouton4 = Button(root, text="convertir", command=B10V16)
Bouton5 = Button(root, text="convertir", command=B2V16)
Bouton6 = Button(root, text="convertir", command=B16V10)

fontStyle = tkFont.Font(family="Lucida Grande", size=45)

fontStyle2 = tkFont.Font(family="Lucida Grande", size=27)


text_variable1 = "base 2 vers base 10"
text_variable2 = "base 10 vers base 2"
text_variable3 = "base 16 vers base 2"
text_variable4 = "base 10 vers base 16"
text_variable5 = "base 2 vers base 16"
text_variable6 = "base 16 vers base 10"


texte_bienvenue = Label(root, text='bienvenue dans le convertiseur de base ', anchor='center', font=fontStyle)

texte1 = Label(root, text=text_variable1, anchor='center', font=fontStyle2)
texte2 = Label(root, text=text_variable2, anchor='center', font=fontStyle2)
texte3 = Label(root, text=text_variable3, anchor='center', font=fontStyle2)
texte4 = Label(root, text=text_variable4, anchor='center', font=fontStyle2)
texte5 = Label(root, text=text_variable5, anchor='center', font=fontStyle2)
texte6 = Label(root, text=text_variable6, anchor='center', font=fontStyle2)


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

root.mainloop()
