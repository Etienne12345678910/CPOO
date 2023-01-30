def getNumber() :
    print("Veuillez encodez un nombre")
    nombre = input()
    return nombre

def somme(nombre1,nombre2) :
    return float(nombre1) + float(nombre2)

def division(somme):    
    return somme / 2



number1 = getNumber()
number2 = getNumber()

sum = somme(number1,number2)

div = division(sum)

print("Le nombre exact est " + str(div))