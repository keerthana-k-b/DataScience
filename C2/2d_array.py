print("SJC23MCA039")
print("Keerthana K B")

import numpy as np
array_2d=np.array([ [1 + 2j, 3 + 4j, 5 + 6j],[7 + 8j, 9 + 10j, 11 + 12j] ],dtype=complex)
print("2D Array: ")
print(array_2d)
rows, columns = array_2d.shape
print("\nNumber of Rows:", rows)
print("\nNumber of Columns:", columns)
dimensions = array_2d.ndim
print("\nDimensions Array :", dimensions)
reshaped_array = array_2d.reshape(3, 2)
print("\nReshaped Array (3*4):")
print(reshaped_array)