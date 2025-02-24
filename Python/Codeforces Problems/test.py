import numpy as np

# Create a symmetric matrix
A = np.array([[1, 2, 3],
              [2, 4, 5],
              [3, 5, 6]])

# Extract the diagonal elements
D = np.diag(A)

print(D)