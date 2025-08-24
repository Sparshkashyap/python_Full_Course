# Calculator 
num1 = int(input("Enter your first number :"))
num2 = int(input("Enter your second number :"))

operator = input("Enter your choice + - / * // ** % :")

if operator == "+":

    print(f"Addition is :{num1+num2}")

elif operator == "-":
    
    print(f"Subtraction  is :{num1-num2}")
    
elif operator == "*":

    print(f"Multiplication is :{num1*num2}")

elif operator == "/":

    print(f"Division is :{num1/num2}")

elif operator == "//":

    print(f"Floor division is :{num1//num2}")
elif operator == "%":

    print(f"Modulas is :{num1%num2}")

else:

    print(f"Exponentation is :{num1**num2}")