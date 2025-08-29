# Problem we are facing in the loops

import numpy as np

prices = [100,200,40,90,50]

discount = 10 #10% of the discount

prices_arr = []

for price in prices:

    actual_price = price - (price*discount/100)
    prices_arr.append(actual_price)

print(prices_arr)


