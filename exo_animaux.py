class Mamifere:
    def __manger__(self):
        print("Je mange ")

    def __son__(self):
        print("Je communique en rugissant")

    def __dormir__(self):
        print("ZZZZZZZ")  



class Aquatique(Mamifere):
    def __init__(self,grogne):
        self.grogne = grogne
        # self.mange = mange
        # self.dodo = dodo

    def groner(self):
        super().__son__()
        print("Mon bruit est " + str(self.grogne))




class Hypo(Aquatique):
     def __init__(self):
         pass
     
     def bruit():
         super().__son__()



bruit = "waaaaa"
mange = "Mangue"
dodo = "La nuit"

hypo = Hypo()

# print("Hypopothame => Le bruit : " + str(hypo.groner) + "Le repas : " + str(hypo.manger) + "Le type de sommeil : " + str(hypo.dodo) )
print("Hypopothame => Le bruit : " + str(hypo.groner())  )



