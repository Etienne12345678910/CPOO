
#test python

#print('Hello world')
#print('Salut les gars')
#ma_variable = 'hello les gars'
#print(type(ma_variable))
#ma_variable = 3
#print(type(ma_variable))
#ma_variable = 'hello'
#ma_variable = ma_variable + 'world'
#print('toto')

#ennonce numero 1
#demandez l age etc etc

#retravailler le code pour mettre d abord celui qui a le plus de chance par exemple 35 ans
#essayez boucle

import random


for i in range(50):

 age = random.randint(1, 100)
 if  age==9 or age==10 :
  print(age, 'Vous etes un poussin')
 elif age==11 or age==12 :    
  print(age, 'Vous etes un  benjamin')
 elif age==13 or age==14 :    
    print(age,'Vous etes un  minime')    
 elif age==15 or age==16 :    
     print(age,'Vous etes un  cadet')
 elif age==17 or age==18 :    
     print(age,'Vous etes un  junior')
 elif age>=19 and age<=34 :    
     print(age,'Vous etes un  senior') 

 else :
     print('Votre age n est pas compris entre 9 et 34 ans')










