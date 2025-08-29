import numpy as np

lis1 = [1,2,3]
lis2 = [4,5,6]

final_val = [x+y for x,y in zip(lis1,lis2)]

print(final_val)