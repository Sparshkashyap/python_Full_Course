from abc import ABC,abstractclassmethod

class Vehicle(ABC):
    @abstractclassmethod
    def start(self):
        pass # no implementation

class Car(Vehicle):
    def start(self):
        print("Car is start")

class Bike(Vehicle):

    def start(self):
        print("Bike is bum bum")


car = Car()
bike = Bike()
# obj = Vehicle() Abstract class ka direct object nhi bana sakte


car.start()
bike.start()


"""
"ABC" ek Abstract class hai which is used to create abstract class
abstractclassmethod ek decorator function hai .
Rule :
1.abstract class ka object nhi bana sakte
2.sabhi class jo abstract class ko inherrit kar rahi hai sabhi mai vo method 
hona important hai jo abstract class mai define kara hai.
3. Abstract class like a blueprint class 

"""