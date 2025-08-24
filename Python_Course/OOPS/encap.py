class Banking:
    def __init__ (self,balance,amount_number):
        self.amount_number = amount_number
        self.__balance = balance # Setter

    def deposit(self,amount):
        self.__balance +=amount
        print(f"New balance is {self.__balance}")

    def get_balance(self): # Getter

        return self.__balance
    

client = Banking(5000,"41923428477")
client.deposit(2000)
print(client.get_balance())
# print(client.__balance) This line give error -> private properties


"""
private variable hide karke rakta hai
getters and setters ki madded sai easily fetch kar sakta hai 
encapculation
"""


