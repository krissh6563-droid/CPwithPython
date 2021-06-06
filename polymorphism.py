"""
The word polymorphism means having many forms. In programming, 
polymorphism means same function name (but different signatures)
"""
def add(a,b,c=0):
    return a+b+c

print(add(2,3))
print(add(2,3,4))

class India:
    def language(self):
        print("Hindi")

class Russia:
    def language(self):
        print("Russia")
obj = India()
obj_1 = Russia()
obj.language()
obj_1.language()