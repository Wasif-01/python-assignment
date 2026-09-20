import numpy as np
from scipy.linalg import lu

A = np.array([
    [4, 1, 0, 0],
    [1, 4, 0, 0],
    [0, 0, 2, 1],
    [0, 0, 1, 2]
])

P, L, U = lu(A)

print("Matrix A:")
print(A)

print("\nP =")
print(P)

print("\nL =")
print(L)

print("\nU =")
print(U)