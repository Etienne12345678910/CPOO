
def getNumber() :
    print("Veuillez encodez un nombre")
    nombre = input()
    return nombre



number = getNumber()
print("Le nombre est : " + str(number))

if(float(number) %2) == 0 :
    print("Le nombre "  + str(number) + " est pair")
else :
    print("Le nombre " + str(number) + " est impair")


