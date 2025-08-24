"""
Without OOPS Programming problems 
1. Low Reusability
2. Low maintance
3. writting like a pain of code
"""

# OOPS
class Character:

    def __init__(self,rollno,name,course): #constructor
        self.rollno = rollno
        self.name = name
        self.course = course

    def details(self):
        print(f"Name of student : {self.name} ,Course of student: {self.course} Roll no: {self.rollno}")


st1=Character(64,"sparsh","BTech")
st2=Character(65,"Neha","BCA")

print(st1.name,st1.course,st1.rollno)
    

"""
1. default constructor (self)
2. parameterized constructor (self,name,color)
3. constructor with default values (self , name="sparsh" , color="Blue")

"""