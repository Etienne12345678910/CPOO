

#f.readlines(2)


def main():
    mon_doc = open("bidon.txt", "r")
    fichier = mon_doc.read()
    print(fichier)
    mon_doc.close()
    # open both files
    with open('bidon.txt','r') as firstfile, open('hello.txt','a') as secondfile:
        for line in firstfile:
            secondfile.write(line)






if __name__ == "__main__":
    main()