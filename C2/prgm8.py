print("SJC23MCA039")
print("Keerthana K B")

import numpy as np
array_1d = np.array([1, 2, 3, 4, 5])
print("\n\n1D Array before insertion:")
print(array_1d)
array_1d = np.insert(array_1d, 2, 6)
print(array_1d)
array_2d = np.array( [ [1, 2, 3],
                      [4, 5, 6] ] )
print("\nOriginal 2D Array:")
print(array_2d)
array_2d = np.insert(array_2d, 1, [7, 8, 9], axis=0)
print("\n2D Array insertions:")
print(array_2d)