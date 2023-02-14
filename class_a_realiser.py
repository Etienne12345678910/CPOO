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

    toto='toto'

    def __init__(self,phrase,toto):
       self.phrase = phrase
       self.phrase = toto   

    def __isPalindrome__(self):
        if self.phrase == self.phrase[::-1]:
            print('C un palindrome')
            return True
        else:
            print('C pas un palin')
            return False

    def __del__(self):
    # actions 
       lala = self.toto.upper()
       print(lala)    



# ete="ete"
# instance = Palindrome().__bool__(ete)
# print(instance)

# albert="albert"
# instance = Palindrome().__isPalindrome__(albert)
# print(instance)

instance = Palindrome('albert','toto')
print(instance.__isPalindrome__())

