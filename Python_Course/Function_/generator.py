
"""def count_num(num):

    while num >0:
        yield num 
        num -=1

for num in range(5):
    print(num) """   

def func():

    yield 1
    yield 2
    yield 3
    yield 4

res = func()
print(next(res))
print(next(res))
print(next(res))
print(next(res))