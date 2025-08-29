import numpy as np

"""
vstack => row wise
hstack => column wise
"""

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])


print(np.hstack((arr1,arr2)))
print(np.vstack((arr1,arr2)))
