class Voiture:

    def __init__(self,vitesse):
        self.vitesse = vitesse
        pass

    def __augmenter__(self):
        self.vitesse += 1
        return str(self.vitesse)
    
    def __ralentir__(self):
        self.vitesse = self.vitesse -1
        return str(self.vitesse)
    def __compteurA0__(self):
        self.vitesse = 0
        return str(self.vitesse)
    
vitesse_de_base = 100
instance = Voiture(vitesse_de_base)
print("Qaund la voiture accelere la vitesse est de " + instance.__augmenter__())
print("Quand la voiture ralentit la vitesse est de " + instance.__ralentir__())
print("Quand la voiture est à l'arret, la vitesse est de " + instance.__compteurA0__())

