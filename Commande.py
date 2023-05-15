from datetime import*
from structure_file import*

class Commande:
    file_commande_en_attente = File()

    def __init__ (self, Utilisateur, Produit, quantité):
        self.achteur = Utilisateur
        self.produit = Produit
        self.qat_commander = quantité
        self.valide = True
        self.validation_commande()
        self.service = False
        self.id = self.id_commande()
        self.vendeur = None
        enfiler(Commande.file_commande_en_attente, self)
        print("Crée Commande : quantité =", quantité ,"id =", self.id , "service=" , self.service,"Prix commande =", self.produit.prix.somme*self.qat_commander, "valisation =", self.valide ,"file commande :", Commande.file_commande_en_attente)

    def validation_commande(self):
        '''
        Entrée : self
        Interne : Verification de la quantité de jeton et de produit nésécaire à la commande
        Sortie : Rien
        '''
        if not self.achteur.jeton.somme >= (self.produit.prix.somme * self.qat_commander) and self.produit.qat >= self.qat_commander :
            self.valide = False
            del self

    def id_commande(self):
        '''
        Entrée : self
        Sortie : id de la commande composée de c + de la date + de l'heure jusqu'au milliseconde
        '''
        date = str(datetime.now())
        id_0 = [date[i] for i in range(4)] + [date[i] for i in range(5,7)] + [date[i] for i in range(8,10)] + [date[i] for i in range(11,13)] + [date[i] for i in range(14,16)] + [date[i] for i in range(17,19)] + [date[i] for i in range(20,23)]
        id = "c"
        for i in range(len(id_0)):
            id = id + id_0[i]
        return(id)

    def commande_servie(self):
        self.service = True
        self.achteur.jeton.retirer_argent(self.produit.prix, self.qat)
        self.produit.retirer_produit(self.qat)
        print("Passer Commande : quantité =", self.qat ,"id =", self.id , "service=" , self.service)
