# # -*- coding
# class MaClass:
#     #
#     #
#     def __init__(self):
#         #do smthg
#         print('toto')
#     pass

# instance = MaClass()
# print(instance)

class Palindrome:

    def __bool__(self,chaineCara):
        if chaineCara == chaineCara[::-1]:
            print('C un palindrome')
            return True
        else:
            print('C pas un palin')
            return False
    

  

# ete="ete"
# instance = Palindrome().__bool__(ete)
# print(instance)

albert="albert"
instance = Palindrome().__bool__(albert)
print(instance)

