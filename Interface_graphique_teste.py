# Créé par Proprietaire, le 16/04/2023 en Python 3.7
from tkinter import*
import tkinter.font as tkFont
from PIL import ImageTk, Image

TAILLE_TEXTE = 15

class interface(Tk):

    def __init__(self):

        Tk.__init__(self)
        self.title("Tests interface graphique")
        self.largeur_fen = int(self.winfo_screenwidth() * 1)
        self.hauteur_fen = int(self.winfo_screenheight() * 0.93)
        self.attributes("-fullscreen", True)

        self.largeur_canvas = int(self.largeur_fen * 0.7)
        self.hauteur_canvas = int(self.hauteur_fen * 0.5)

        self.font_texte = tkFont.Font(family='Helvetica', size=TAILLE_TEXTE, weight='bold')

        self.accueil()

    def accueil(self):

        #Zone 1
        self.zone1 = Frame(self)
        self.zone1.grid(row=1,column=1,padx=10,pady=10)

        #Bonton Profil
        self.photo_profil = ImageTk.PhotoImage(file='image_profil_2.jpg')
        self.bouton_profil = Button(self.zone1)
        self.bouton_profil.configure(image= self.photo_profil, width = 50, height = 50 )
        self.bouton_profil.grid(row=1,column=1,padx=0,pady=0)

        #Zone 2
        self.zone2 = Frame(self)
        self.zone2.grid(row=2, column=2, padx=(self.largeur_fen-self.largeur_canvas-140)/2, pady=0)

        self.can = Canvas(self.zone2)
        self.can.configure(width = self.largeur_canvas, height = self.hauteur_canvas, bg="white")

        #Jeton
        image_jeton = Image.open("logo_jeton_teste.png")
        rapport = image_jeton.size[0]/self.largeur_canvas
        image_jeton = image_jeton.resize((int(image_jeton.size[0]*rapport),int(rapport*image_jeton.size[1])))    #  on s'adapte à la taille du canvas
        image_jeton.save("logo_jeton_teste_redim.png")
        self.image_jeton = PhotoImage(file="logo_jeton_teste_redim.png")
        self.can.create_image((self.largeur_canvas - image_jeton.size[0])/2, (self.hauteur_canvas - image_jeton.size[1])/2, image=self.image_jeton)
        self.can.pack()

        #Zone 3
        self.zone3 = Frame(self)
        self.zone3.grid(row=1,column=3,padx=10,pady=10)

        #Bouton Menu
        self.image_menu = ImageTk.PhotoImage(file='menu_butom.png')
        self.bouton_menu = Button(self.zone3)
        self.bouton_menu.configure(image= self.image_menu, width = 50, height = 50)
        self.bouton_menu.grid(row=1,column=1,padx=0,pady=0)

        #Zone 4
        self.zone4 = Frame(self)
        self.zone4.grid(row = 3, column = 2, padx = 10, pady = 10)

        self.bouton_historique = Button(self.zone4)
        self.bouton_historique.configure(text = "Historique\nachat", width = 10, height = 10, bg = "white" )
        self.bouton_historique.grid(row=1,column=1,padx=0,pady=0)


app = interface()
app.mainloop()
