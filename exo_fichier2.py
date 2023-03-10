import pdb

def main():
    mon_doc = open("bidon.txt", "r")
    fichier = mon_doc.read()
    fichier = open("bidon.txt", "a")
    nom = input()
    prenom = input()
    profession = input()
    fichier.write("\n" + nom + " " + prenom + " " + profession + "\n" )
    pdb.set_trace()
    lire = mon_doc.readlines()   
    print(lire)
    pdb.set_trace()

    pass


if __name__ == "__main__":
    main()