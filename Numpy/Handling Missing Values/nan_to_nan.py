import numpy as np

arr = np.array([1,2,np.nan,4,np.nan])

clened_arr = np.nan_to_num(arr,nan=100)

print(clened_arr)