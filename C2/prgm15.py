print("SJC23MCA039")
print("Keerthana K B")

import numpy as np
def is_symmetric(matrix):
  return (matrix == matrix.T).all()
def is_skew_symmetric(matrix):
  return (matrix == -matrix.T).all()
matrix = np.array([[0, 1, -2],
[-1, 0, 3],
[2, -3, 0]])

if is_symmetric(matrix):
   print("The matrix is symmetric.")
elif is_skew_symmetric(matrix):
   print("The matrix is skew-symmetric.")
else:
  print("The matrix is neither symmetric nor skew-symmetric.")