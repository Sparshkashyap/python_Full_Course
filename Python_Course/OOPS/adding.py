class Car:
    def car_details(self,color,name):

        self.color = color
        self.name = name

        print(f"The color is :{self.color} and name is {self.name}")

c1 = Car()
c1.car_details("Red","Tesla")