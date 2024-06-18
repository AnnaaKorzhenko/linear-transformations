import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

def find_eigen(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)

    for i in range(len(eigenvalues)):
        lambda_i = eigenvalues[i]
        v_i = eigenvectors[:, i]

        Av = np.dot(matrix, v_i)

        lambda_v = lambda_i * v_i

        if np.allclose(Av, lambda_v):
            print(f"Eigenvalue {lambda_i} and corresponding eigenvector {v_i} satisfy the equation A⋅v = a⋅v")
        else:
            print(f"Eigenvalue {lambda_i} and corresponding eigenvector {v_i} do NOT satisfy the equation A⋅v = a⋅v")

    return eigenvalues, eigenvectors