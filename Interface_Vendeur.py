from Jeton import*
from Produit import*
from Commande import*
from structure_file import*
from threading import Thread


class Vendeur :
    liste_vendeur = []

    def __init__ (self, nom):
        self.teste = True
        self.nom = nom
        self.liste_vendeur.append(self)
        self.liste_commande_en_attente = File()
        self.liste_commande_distribuer = []
        self.etat = False                           #True = Vendeur connecter,   False = Vendeur non connecter ou en fin de service
        self.action = True                         #True = En attente commande, False = Prépare une commande
        print("Crée :",self.nom,"etat :", self.etat,"action :",self.action)

    def prepa_com(self):
        if self.action :
            self.action = False
            commende_en_prepa = defiler(self.liste_commande_en_attente)
            while not self.action :
                None
            self.liste_commande_distribuer = commende_en_prepa + self.liste_commande_distribuer
        elif not estVide(self.liste_commande_en_attente):
            self.prepa_com()



    def commande_est_donner(self, Commande):
        commande_d = Commande_a_donner(Commande, self)
        Commande.service = True
        distrib_commande = commande_d
        self.liste_commande_distribuer = self.liste_commande_distribuer + [distrib_commande]
        print("Commande donné : ", Commande, "liste commande v = ", self.liste_commande_distribuer, "Par :", self.nom)

Julien = Vendeur("jul")
Gérard = Vendeur("ger")
Jean_Luc = Vendeur("jea")

def recherche_vendeur():
    print("oui")
    while not estVide(Commande.file_commande_en_attente) :
        for vend in Vendeur.liste_vendeur :
            if vend.etat :
                print("envoie commande")
                vend.liste_commande_en_attente.enfiler(defiler(Commande.file_commande_en_attente))
