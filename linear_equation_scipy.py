import numpy as np
from scipy.linalg import solve

# 1
A = np.array([
    [2, 3],
    [4, 5]
])

B = np.array([8, 14])

x, y = solve(A, B)

print("1.")
print("x =", x)
print("y =", y)


# 2
A = np.array([
    [1, -1],
    [1,  1]
])

B = np.array([1, 11])

x, y = solve(A, B)

print("\n2.")
print("Velocity of Car 1 =", x)
print("Velocity of Car 2 =", y)