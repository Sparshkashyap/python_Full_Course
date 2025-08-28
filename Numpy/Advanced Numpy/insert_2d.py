import numpy as np

arr = np.array([[1,2],[4,5]])
print(arr)
new_2d = np.insert(arr,0,[5,10],axis=None) # Normal 1d mai convert ho jayga
new_2d = np.insert(arr,0,[5,10],axis=1) # Column wise insert hogi value
new_2d = np.insert(arr,0,[5,10],axis=0) # row wise insert hogi value
print(new_2d)