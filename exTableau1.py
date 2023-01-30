
 
#coding: utf-8
def swapList(L):
    # obtenir le dernier élément de la liste
    swap = L[-1]
    
    # remplacer le dernier élément de la liste par le premier
    L[-1] = L[0]
    
    # remplacer  le premier élément de la liste par le dernier
    L[0] = swap
    return L
    
    
# Exemple   
L = ["Python" , "Java" , "C++" , "Javascript"]
print(swapList(L))
# La sortie est  : ['Javascript', 'Java', 'C++', 'Python']