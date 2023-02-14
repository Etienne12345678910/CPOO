from random import *
class Utilisateur:
     def __init__(self):
        pass
       
     def __play__(self):
        print('Quel est votre choix ?')
        player = input("Pierre\nPapier\nCiseaux\n")
        #while player not in ["pierre","papier","ciseaux"]:
            #player = input("pierre\npapier\nciseaux\n")
        return (player)
     
class Ordinateur:
    def __init__(self):
        pass

    def __play__(self):
        n = randint(1,3)
        if n == 1:
            ordi = "pierre"
        elif n==2:
         ordi = "papier"
        else:
         ordi = "ciseaux"
        return(ordi)    
    
   
a = Utilisateur()
b = Utilisateur()

nombre1 = a.__play__()
nombre2 = b.__play__()

print(nombre1)
print('-------------------------------------------------------------------------')
print(nombre2)
print('-------------------------------------------------------------------------')

if(nombre1 == nombre2):
    print('C Gagne')
else:
    print('Perdu')


    