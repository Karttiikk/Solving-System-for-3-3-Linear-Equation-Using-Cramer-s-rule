import numpy as np
u = np.array([[1, 1, 1], [2, 3, -1], [3, 4, 5]])
v = np.array([6, 5, 26])
def det(matrix):
    return np.linalg.det(matrix)
def solve_cramer(u, v):
    det_u = det(u)
    det_x = det(np.column_stack((v, u[:, 1:],)))
    det_y = det(np.column_stack((u[:, 0], v, u[:, 2])))
    det_z = det(np.column_stack((u[:, :2], v)))
    x = det_x / det_u
    y = det_y / det_u
    z = det_z / det_u
    return x, y, z
x, y, z = solve_cramer(u, v)
print("x = ", x)
print("y = ", y)
print("z = ", z)
