
"""
.flatten() => copy of array
.ravel()   => view original array

"""

import numpy as np

arr =  np.array([[1,2,3],[4,5,6],[7,7,8]])

print(arr.ravel())
print(arr.flatten())

