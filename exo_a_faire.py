from random import *
class pierrePapierCiseux:
     def __init__(self,humain,machine):
        self.humain = humain
        self.machine = machine
        pass

     def __player__(self):
        print('Quel est votre choix ? \nPierre\nPapier\nCiseaux\n')
        self.humain = input()
        # return choix
     def __ordinateur__(self):
        n = randint(1,3)
        if n == 1:
         self.machine = "pierre"
        elif n==2:
         self.machine = "papier"
        else:
         self.machine = "ciseaux"
        return(self.machine)

homme = pierrePapierCiseux()
machine = pierrePapierCiseux()

Pierre = homme.__player__()
Ordi = machine.__ordinateur__()

print(Pierre)
print('------------------')
print(Ordi)

print('------------------')

if Pierre == Ordi:
    print('C gagne')
else:
    print('Perdu')    