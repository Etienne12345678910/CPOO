import csv

def recherche_personne(nom, prenom, profession, fichier):
    with open(fichier, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == nom and row[1] == prenom and row[2] == profession:
                return True
    return False

def ajouter_personne(nom, prenom, profession, fichier):
    with open(fichier, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([nom, prenom, profession])

def modifier_personne(nom, prenom, profession, fichier):
    lignes = []
    with open(fichier, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == nom and row[1] == prenom and row[2] == profession:
                choix = input("Cette personne est déjà présente dans le fichier. Voulez-vous modifier ses données ? (O/N) ")
                if choix == "O":
                    nouveau_nom = input("Entrez le nouveau nom : ")
                    nouveau_prenom = input("Entrez le nouveau prénom : ")
                    nouvelle_profession = input("Entrez la nouvelle profession : ")
                    lignes.append([nouveau_nom, nouveau_prenom, nouvelle_profession])
                else:
                    lignes.append(row)
            else:
                lignes.append(row)
    with open(fichier, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(lignes)

def supprimer_personne(nom, prenom, profession, fichier):
    lignes = []
    with open(fichier, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == nom and row[1] == prenom and row[2] == profession:
                choix = input("Cette personne est déjà présente dans le fichier. Voulez-vous supprimer ses données ? (O/N) ")
                if choix != "O":
                    lignes.append(row)
            else:
                lignes.append(row)
    with open(fichier, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(lignes)

def main():
    nom = input("Entrez votre nom : ")
    prenom = input("Entrez votre prénom : ")
    profession = input("Entrez votre profession : ")
    fichier = "personnes.csv"

    if recherche_personne(nom, prenom, profession, fichier):
        choix = input("Cette personne est déjà présente dans le fichier. Voulez-vous modifier ou supprimer ses données ? (M/S/N) ")
        if choix == "M":
            modifier_personne(nom, prenom, profession, fichier)
            print("Les données ont été modifiées avec succès.")
        elif choix == "S":
            supprimer_personne(nom, prenom, profession, fichier)
            print("Les données ont été supprimées avec succès.")
        else:
            print("Les données n'ont pas été modifiées.")
    else:
        ajouter_personne(nom, prenom, profession, fichier)
        print("Les données ont été ajoutées avec succès.")

