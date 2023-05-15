from datetime import*
from Interface_Vendeur import*
from Commande import*

class Utilisateur():
    liste_Utilisateur = []

    def __init__ (self,jeton):
        self.liste_Utilisateur = self.liste_Utilisateur + [self]
        self.jeton= Jeton(jeton)
        self.commande_passer = []
        print("Crée Martin : jeton =", self.jeton.somme, "commande passer =",self.commande_passer)

    def achat(self, Produit, quantité):
        '''
        Entrée : self et une somme d'argent
        Interne : Création de la comande et ajout si commande valide a la liste des commande effectuer la commande
        Sortie : Rien
        '''
        commande = Commande(self, Produit, quantité)
        if commande.valide :
            self.commande_passer = self.commande_passer + [commande]
            print("Achat Cafe : quantité demander = ", quantité, "quantité retant =",Produit.qat)
            print("Achat Martin : jeton =", self.jeton.somme, "commande passer =",self.commande_passer)
        else :
            del commande

Martin = Utilisateur(45)
Martin.achat(Cafe, 1)