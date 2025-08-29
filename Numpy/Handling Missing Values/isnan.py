import numpy as np

arr = np.array([1,2,np.nan,3,np.nan,5])

print(np.isnan(arr))

print(np.nan == np.nan)