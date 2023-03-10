# import pdb
# mon_doc = open("hello.txt", "r")
# print(mon_doc)
# fichier = mon_doc.read()
# print(fichier)
# #Ceci n’est pas un fichier
# mon_doc.close()

# mon_doc = open("hello.txt", "w")
# mon_doc.write("Je vous dit que c’est un fichier,moi !")
# pdb.set_trace()
# #Q / C
# mon_doc.close()

from pathlib import Path
import os

def main():
    # marche si fichier ailleurs
    p = Path('toto.txt').resolve()
    print(p)
    # marche si fichier au meme endroit
    mon_doc = open("hello.txt", "r")
    print(mon_doc)
    fichier = mon_doc.read()
    print(fichier)
    #Ceci n’est pas un fichier
    mon_doc.close()
    current = os.getcwd()
    open(f'{current}/hello.txt', 'r')
    print(current)
    # current = os.getcwd()
    # open(f’{current}/dossier/truc.txt’, ‘r’)

    




if __name__ == "__main__":
    main()