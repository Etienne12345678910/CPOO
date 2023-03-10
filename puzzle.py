class Puzzle:
     def __init__(self,t):
        self.t = t
        #pass

     def __y__(self,t):
        return len(t) 

a = 'toto'
instance = Puzzle(a)
instance2 = 'toto'
variable = Puzzle(instance2)
#variable = instance2
print(variable is Puzzle(a))

