import numpy as np

A = np.array([
    [3, -5],
    [4, -2]
])

B = np.array([10, 7])

x, y = np.linalg.solve(A, B)

print("x =", x)
print("y =", y)