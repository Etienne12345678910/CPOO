#faire class humain, ordinateur et jeu
from random import *
class humain:
     def __init__(self):
        pass

     def __jeux__(self):
        print('Quel est votre choix ? \nPierre\nPapier\nCiseaux\n')
        self.humain = input()

class ordinateur:
        def __init__(self):
         pass

        def __ordinateur__(self):
         n = randint(1,3)
         if n == 1:
          self.machine = "pierre"
         elif n==2:
          self.machine = "papier"
         else:
          self.machine = "ciseaux"
         return(self.machine)

class jeux:
        def __init__(self,mot1,mot2):
            self.mot1 = mot1
            self.mot2 = mot2
          

        def __play__(self):
              if self.mot1 == self.mot2:
                print('C gagne')
              else:
                print('C perdu')


instance = humain()
instance2 = ordinateur()
instance3 = jeux(instance,instance2)

mot_humain = instance.__jeux__()
mot_ordi = instance2.__ordinateur__()

# instance3.__jeux__(mot_humain,mot_ordi)

instance3.__play__()
print(instance3)