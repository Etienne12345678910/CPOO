class Form():
    def perimeter(self):
        print("Le perimetre")


class Triangle(Form):
    def __init__(self,cote1,cote2,cote3):
        self.cote1 = cote1
        self.cote2 = cote2
        self.cote3 = cote3

    def perimetre(self):    
        perimeter = self.cote1 + self.cote2 + self.cote3


print("Valeur 1 : \n")
valeur1 = input()
print("Valeur 2 : \n")
valeur2 = input()
print("Valeur 3 : \n")
valeur3 = input()
triangle = Triangle(valeur1,valeur2,valeur3)
print("le résultat est :  " + str(triangle.perimeter()))


