import numpy as np

# NumPy se structured data read karna (Pandas se easy hota hai)
data = np.genfromtxt('Used_Bikes.csv', delimiter=',', dtype=None, encoding='utf-8', names=True)

# Print karna
print(data)

# Kisi column ko access karna (e.g. price)
print(data['price'])
