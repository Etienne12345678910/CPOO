def getWord():
    print("Veuillez encoder un mot")
    mot = input()
    mot = mot.replace(" ", "")
    return mot

def nbrLettre(w):
    return len(w)    


word = getWord()

number = nbrLettre(word)

print("Le nombre de lettre dans le mot est de : " + str(number))