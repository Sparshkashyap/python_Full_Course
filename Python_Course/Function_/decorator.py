
def my_decorator(fuc):

    def wrapper():

        print("Something happening before the function called")
        fuc()
        print("Something happining After the function called")

    return wrapper


@my_decorator
def sayhello():

    print("Hello")

sayhello()