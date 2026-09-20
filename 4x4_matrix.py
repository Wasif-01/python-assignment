import numpy as np
from scipy.linalg import svd

# Create 4x4 matrix
A = np.array([
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [1, 3, 5, 7],
    [2, 5, 8, 11]
])

# Find transpose
transpose = A.T

# Find rank using SciPy SVD
U, S, Vt = svd(A)
rank = np.sum(S > 1e-10)

print("Matrix A:")
print(A)

print("\nTranspose of A:")
print(transpose)

print("\nRank of A:")
print(rank)