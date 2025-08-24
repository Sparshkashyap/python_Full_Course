
"""lis = [] 

for i in range(1,11):

    lis.append(i**2)

print(lis)"""

"Used List comprehension"


res = [i ** 2 for i in range(1,10)]
rest = [i ** 2 for i in range(1,10) if i%2==0]

print(res)
print(rest)