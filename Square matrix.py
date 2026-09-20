import numpy as np


A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 10]
])

print("Original Matrix:")
print(A)
A_inv = np.linalg.inv(A)
print("i) Inverse of A:\n", A_inv)

A_A_inv = np.dot(A, A_inv)
print("\niii) Result of A @ A^-1 (Identity Matrix):\n", np.round(A_A_inv, 4))

Q, R = np.linalg.qr(A)

print("\nQ Matrix:")
print(Q)

print("\nR Matrix:")
print(R)

print("\nCheck Q @ R:")
print(Q @ R)


U, S, VT = np.linalg.svd(A)

print("\nU Matrix:")
print(U)

print("\nSingular Values:")
print(S)

print("\nVT Matrix:")
print(VT)

S_matrix = np.diag(S)

print("\nS Matrix:")
print(S_matrix)

print("\nCheck U @ S @ VT:")
print(U @ S_matrix @ VT)


qr_list = [Q, R]

print("\nQR as a List:")
print(qr_list)

print("\n--- Question 2 ---")

eq_coeffs = np.array([[2, 3], 
                      [4, 2]])
eq_vals = np.array([8, 14])

solution = linalg.solve(eq_coeffs, eq_vals)
print("i) Solution for linear equations (x, y):", solution)


distance = 11 
car_coeffs = np.array([[11, -11], 
                       [1, 1]])
car_vals = np.array([distance, distance])

velocities = linalg.solve(car_coeffs, car_vals)
print(f"ii) Velocities of the cars (assuming distance=11): v1={velocities[0]}, v2={velocities[1]}")