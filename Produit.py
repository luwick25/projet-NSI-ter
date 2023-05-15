from Jeton import*

class Produit:
    liste_produit = []

    def __init__(self, prix, quantité):
        self.liste_produit += [self]
        self.prix = Jeton(prix)
        self.qat = quantité
        print("Crée Café : prix =", self.prix.somme, "quantité =",self.qat)

    def retirer_produit(self, qat):
        '''
        Entrée : self et une quantité de produit
        Interne : Modification du nombre de Produit en stock ( version ajouter )
        Sortie : Rien
        '''
        self.qat = self.qat - qat
        print("Retire Café : prix =", self.prix,"quantité retirer :", qat, "quantité actuelle=",self.qat)

Cafe = Produit(5, 10)

