from tkinter import *


def choix():
    import main
    v = main.enter_du_choix.get()
    main.root.destroy()
    if v == '1':
        B2V10(main.n)
    elif v == '2':
        B2V10(main.n)
    elif v == '3':
        B2V10(main.n)
    elif v == '4':
        B2V10(main.n)
    elif v == '5':
        B2V10(main.n)
    elif v == '6':
        B2V10(main.n)
    else:
        print ("votre choix n'est pas valide")


def B2V10():
    import main
    main.window2.destroy()
    nbf = int(main.n, 2)
    window3 = Tk()
    window3.title("A")
    rep = Label(window3, text=nbf)
    rep.pack()
    window3.mainloop()


def B10V2(n):
    import main
    main.window2.destroy()
    window3 = Tk()
    window3.title("B")
    nbf = []
    while n != 0:
        bi = n % 2
        n = n // 2
        nbf = nbf + [bi]

    rep = Label(window3, text=nbf)
    rep.pack()
    window3.mainloop()


def B16V2():
    import main
    main.window2.destroy()
    window3 = Tk()
    window3.title("C")
    nbd = int(main.n, 16)
    nbf = []
    while nbd != 0:
        bi = nbd % 2
        nbd = nbd // 2
        nbf = nbf + [bi]
    nbf.reverse()
    rep = Label(window3, text=nbf)
    rep.pack()
    window3.mainloop()


def B10V16():
    import main
    main.window2.destroy()
    window3 = Tk()
    window3.title("D")
    nbf = hex(int(main.n))
    rep = Label(window3, text=nbf)
    rep.pack()
    window3.mainloop()


def B2V16():
    import main
    main.window2.destroy()
    window3 = Tk()
    window3.title("E")
    nbf = hex(int(main.n, 2))
    rep = Label(window3, text=nbf)
    rep.pack()
    window3.mainloop()


def B16V10():
    import main
    main.window2.destroy()
    window3 = Tk()
    window3.title("F")
    nbf = int(main.n, 16)
    rep = Label(window3, text=nbf)
    rep.pack()
    window3.mainloop()
