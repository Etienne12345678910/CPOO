class Multiplication:
     def __init__(self,entier):
        self.entier = entier
        #pass

     def __doMultiplication__(self):
        
        #print('Quel est votre entier ?')
        #self.entier = input()
        self.entier= int(self.entier)*int(self.entier)
        #print(int(self.entier))
        return self.entier

print('Quel est votre entier ?')
choix = input()
instance = Multiplication(choix)
print(instance.__doMultiplication__())