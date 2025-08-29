import numpy as np

prices = np.array([100,200,300,500,600,700])

discount = 10 # 10% of the discount

final_value = prices - (prices*discount/100)

print(final_value)