import random

def getRandomNumber():
    nbr = random.randint(1, 100)
    return nbr


nombre = getRandomNumber()


for i in range(10) :
    pense = input("A quel nombre pensez-vous ? \n")
    pense = int(pense)
    if pense < nombre :
        appreciation = "trop bas"
        print(pense, appreciation)
    else :
        appreciation = "trop haut"
        print(pense, appreciation)
    if pense == nombre:
        appreciation = "bravo !"
        print(pense, appreciation)
        break
