class Mamifere:
    def __manger__(self):
        print("Je mange ")

    def __son__(self):
        print("Je communique en rugissant")

    def __dormir__(self):
        print("ZZZZZZZ")    





class Hypo(Mamifere):
    def __init__(self,grogne):
        self.grogne = grogne
        # self.mange = mange
        # self.dodo = dodo

    def groner(self):
        super().__son__()
        # print( str(super().__son__()) + str(self.grogne)  )
        

    # def manger(self):
    #     super().__manger__()
    #     print("Je mange des " + self.mange )

    # def dodo(self):
    #     super().__dormir__()
    #     print("Je dors " + self.dodo)

bruit = "waaaaa"
mange = "Mangue"
dodo = "La nuit"

hypo = Hypo(str(bruit))

# print("Hypopothame => Le bruit : " + str(hypo.groner) + "Le repas : " + str(hypo.manger) + "Le type de sommeil : " + str(hypo.dodo) )
print("Hypopothame => Le bruit : " + str(hypo.groner())  )


# class Lion(Mamifere):
#     def __init__(self):

#         pass                
# class Tigre(Mamifere):
#     def __init__(self):
#         pass

# class Loup(Mamifere):
#     def __init__(self):
#         pass
