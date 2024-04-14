from abc import ABC, abstractmethod

class Car(ABC):
    
    #constructor
    def __init__(self,brand,model, year):
        self.brand = brand
        self.model = model
        self.year = year

    #abstract method
    @abstractmethod
    def print_details(self):
        pass

    #concreate method
    def accelarate(self):
        print("Speed up.....")
    
    def break_applied(self):
        print("Stop...")

#child class
class hatchback(Car):

    def print_details(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Year:",self.year)

    def Sunroof(self):
        print("Not having this feature")

    
#child class
class suv(Car):

    def print_details(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Year:",self.year)

    def sunroof(self):
        print("Available")

obj = suv("Maruti","Alto",2020)
obj.print_details()
obj.accelarate()


