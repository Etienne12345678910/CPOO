class Division:
    def __init__(self,numerateur,denominateur):
        self.numerateur = numerateur
        self.denominateur = denominateur
        #self.fraction = fraction
        #pass

    def __numerateur__(self):
        #self.numerateur = input()
        return int(self.numerateur)

    def __denominateur__(self):
        #self.denominateur = input()
        if self.denominateur == 0:
            print('Un denominateur ne peut être égal à 0')
            return 
        else:
            return int(self.denominateur)

    def __fration__(self):
        self.fraction = float(self.numerateur)/float(self.denominateur)
        print(float(self.fraction))


numerateur = input()
denominateur = input()
#resultat = input()
instance = Division(numerateur,denominateur)
print(instance.__fration__())



