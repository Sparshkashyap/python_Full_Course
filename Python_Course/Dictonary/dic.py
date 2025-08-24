
dict = {
    "lis":[1,2,3],
    "tup":(1,2.3,4),

}

dict["price"] = 100

dict["price"] = 50

del dict["price"]

res = dict.keys()

rst = dict.values()

result = dict.items()

poped = dict.pop("ls","Not found")

print(poped)
print(dict)
# print(list(res))
# print(list(rst))
# print(list(result))