import tkFont

from tkinter import *

from main2 import choix


root = Tk()

root.title(' convertiseur de base ')

root.minsize(1920, 1080)

enter_du_choix = Entry(root)

Bouton = Button(root, text="enter", command=choix)

fontStyle = tkFont.Font(family="Lucida Grande", size=45)

fontStyle2 = tkFont.Font(family="Lucida Grande", size=27)

texte_bienvenue = Label(root, text='bienvenue dans le convertiseur de base ', anchor='center', font=fontStyle)

texte = Label(root, text="faite votre choix\n"
                         "choix 1: base 2 vers base 10 \n"
                         "choix 2: base 10 vers base 2 \n"
                         "choix 3: base 16 vers base 2 \n"
                         "choix 4: base 10 vers base 16 \n"
                         "choix 5: base 2 vers base 16 \n"
                         "choix 6: base 16 vers base 10 \n", anchor='center', font=fontStyle2)

texte_bienvenue.pack()

texte.pack()

enter_du_choix.pack()

Bouton.pack()

root.mainloop()


window2 = Tk()

window2.title("2")

window2.minsize(1920, 1080)

fontStyle2 = tkFont.Font(family="Lucida Grande", size=27)

enter_du_nombre = Entry(window2)

n = enter_du_nombre.get()

Bouton2 = Button(window2, text="enter")

texte2 = Label(window2, text="Entrer le nombre que vous souhaitez convertir", anchor='center', font=fontStyle2)

texte2.pack()

enter_du_nombre.pack()

Bouton2.pack()

window2.mainloop()