"""
Without OOPS Programming problems 
1. Low Reusability
2. Low maintance
3. writting like a pain of code
"""

# OOPS
class Character:

    def __init__(self,rollno,name,course):
        self.rollno = rollno
        self.name = name
        self.course = course

    def details(self):
        print(f"Name of student : {self.name} ,Course of student: {self.course} Roll no: {self.rollno}")


st1=Character(64,"sparsh","BTech")
st2=Character(65,"Neha","BCA")

# st1.details()
# st2.details()
        