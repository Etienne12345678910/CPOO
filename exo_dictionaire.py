
#essais fonction

iron_man = {'nom': 'Dupont', 'prenom': 'Davi', 
'age':  '30'}

#corriger dans le prénom avec la bonne valeur ‘David

iron_man.update({'prenom' : 'David'})

# print(iron_man)

# print('Clés : ')
# for v in iron_man.keys():
#     print(v)

# print('Valeurs : ')
# for v in iron_man.values():
#     print(v)

# print('Clés - Valeurs')
# for k,j in iron_man.items():
#     print(f'{k}-{j}')

# print(f"{iron_man['prenom']} {iron_man['nom']} a {iron_man['age']}")    

# iron_man['date_naissance'] = '11/02/1953'

# print(iron_man)



mon_dico={'nom' : 'Jean' , 'prenom' : 'Dupont','age' : '45 ans'}
print(mon_dico)

mon_dico.update({'pays' : 'Belgique'})
print(mon_dico)

mon_dico['Localite']='Hainaut'
print(mon_dico)

print("Les clés : ")
for i in mon_dico.keys():
    print(i)

print("Les valeurs : ")    
for j in mon_dico.values():
    print(j)


