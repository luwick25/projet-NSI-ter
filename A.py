from tkinter import *
from tkinter import ttk




fenetre = Tk()
fenetre.geometry('300x500')
fenetre.title("connexion/creation")




#######################################################################################
                        ###zone de setup de l'inscription/ connexion
#######################################################################################


class Id:
    def __init__(self, nom):
        self.nom = nom

class Mdp :
    def __init__ (self, mot_de_passe):
        self.mot_de_passe = mot_de_passe

class Compte:

    def __init__ (self, nom, mot_de_passe):
        self.nom = nom
        self.mot_de_passe = mot_de_passe




class Liste:

    def __init__(self):
        self.liste_compte = []

    def ajout(self,Id, Mdp):

        if self.verfication_ajout(Id):
            self.liste_compte = self.liste_compte + [Compte(Id, Mdp)]
            return 'Compte ajoutée'

        else :
            return 'nom ' +"'"+Id.nom+"'" +' deja utilisée' '\n'


    def verfication_ajout(self, Id):

        for i in range(len(self.liste_compte)):

            if self.liste_compte[i].nom.nom == Id.nom:
                return False
        return True

    def journal_compte(self):

        for i in range(len(self.liste_compte)):
            print(self.liste_compte[i].nom , ": " , self.liste_compte[i].mot_de_passe)

######################################################################################
                        ###VERIFICATION DE CHAQUE PARAMETRE
######################################################################################

    def connexion_mot_de_passe(self,Mdp):

        for i in range(len(self.liste_compte)):

            if self.liste_compte[i].mot_de_passe.mot_de_passe == Mdp.mot_de_passe:
                return True
        return False

    def connexion_nom(self,Id):

        for i in range(len(self.liste_compte)):

            if self.liste_compte[i].nom.nom == Id.nom:
                return True
        return False

#######################################################################################
                        ###connexion final
#######################################################################################

    def connexion(self,Id,Mdp):
        if self.connexion_mot_de_passe(Mdp) == True:
            if self.connexion_nom(Id) == True:
                print ("bonjour " + "'"+Id.nom+"'")
            else:
                print( "mot de passe ou Identifiant incorrect" '\n')
        else:
            print( "mot de passe ou Identifiant incorrect" '\n')



Liste_Pseudo = Liste()


def Journal_des_compte():
    Liste_Pseudo.journal_compte()



def recupere_Id():
    pseudo= Id(value.get())
    print(pseudo)


def recupere_mot_de_passe():
    Mdp = Mdp(value2.get())
    print(Mdp)


def creation():
    print(Liste_Pseudo.ajout(Id(entree.get()), Mdp(entree2.get())))


def connexion():
    Liste_Pseudo.connexion(Id(entree.get()), Mdp(entree2.get()))






#######################################################################################
#recuperation Identifiant
#######################################################################################

Frame3 = Frame(fenetre, borderwidth=2)
Frame3.place(x=150, y=100, anchor=CENTER)


value = StringVar()
value.set("Identifiant")
entree = Entry(Frame3, textvariable=value, width=30)
entree.pack()


######################
#recuperer mot de passe
######################

Frame2 = Frame(fenetre, borderwidth=2, pady=5)
Frame2.place(x=150, y=200, anchor=CENTER)


value2 = StringVar()
value2.set("mot de passe")
entree2 = Entry(Frame2, textvariable=value2, width=30)
entree2.pack()


######################
#boutton de creation
######################
bouton3 = Button(text="créé votre Compte", command=creation,padx=10, pady=10)
bouton3.place(x=150, y=300, anchor=CENTER)


######################
#bouton de connexion
######################
bouton4 =Button(text="connexion",command=connexion,padx=10, pady=10)
bouton4.place(x=150, y=375,anchor=CENTER)




fenetre.mainloop()
