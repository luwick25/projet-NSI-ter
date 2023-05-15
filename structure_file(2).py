from collections import deque

class File :

    def __init__(self):
        self.contenu = deque([])

    def __repr__(self):
        ch=" Entrée |"
        for i in self.contenu:
            ch += " "+str(i)
        return ch + " | Sortie"

    def estVide(self) :
        return len(self.contenu) == 0

    def enfiler(self, x):

        self.contenu.appendleft(x)

    def defiler(self):
        assert not self.estVide(), "la file est vide"
        return self.contenu.pop()

def afficher(f):
    print(f)

def enfiler(f,element):
    f.enfiler(element)

def defiler(f):
    return f.defiler()

def estVide(f):
    return f.estVide()








