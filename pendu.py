class Pendu:
    def __init__(self,mot,lettre):
        self.mot = mot
        self.lettre = lettre
        pass

    def __chercher__(self):    
        if self.lettre in self.mot:
            print("La lettre est présente ")
        else:
            print("La lettre n est pas présente")

mot = 'toto'
print("Veuillez encodez une lettre \n")
lettre = input()

for lettre  in mot:
    instance = Pendu(mot,lettre)
    print(instance.__chercher__())
