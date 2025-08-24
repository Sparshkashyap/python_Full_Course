# polimorphism with class method overridding

class Bird():

    def sound(self):
        print("Chu Chu heee")

class Cow(Bird):

    def sound(self):
        print("cow is maee maee")

class Parrat(Bird):

    def sound(self):
        print("parrat is kua kua")

obj1 =Cow()
obj2 = Parrat()

obj1.sound()
obj2.sound()