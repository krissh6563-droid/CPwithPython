#Private access specifier
# only accessable within the class
class Person:
    __name = "Krishna"
    __age = 20
    
    def __func(self):
        print("This is protected function")
        

    def func_1(self):
        print(self.__age)

obj = Person()
obj.__func()

