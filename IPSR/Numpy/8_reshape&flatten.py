import numpy as np
arr = np.arange(1, 13)
print("Original:", arr)
reshaped = arr.reshape(3, 4)
print("Reshaped:\n", reshaped)
flattened = reshaped.flatten()
print("Flattened:", flattened)
