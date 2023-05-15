class Jeton():                                         #Création du système de monnaie

    def __init__ (self, somme):
        self.somme=somme

    def ajouter_argent(self, gain):
        '''
        Entrée : self et une somme d'argent
        Interne : Modification du nombre de Jeton ( version ajouter )
        Sortie : Rien
        '''
        self.somme= self.somme + gain

    def retirer_argent(self, perte, qat = 1):
        '''
        Entrée : self et une somme d'argent
        Interne : Modification du nombre de Jeton ( version retirer )
        Sortie : Rien
        '''
        self.somme = self.somme - perte*qat

