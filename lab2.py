import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread


# func for finding the eigenvectors and eigenvalues 
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

# original image
image_in_color = imread("myimage.jpg")

print(f"Висота, ширина, канали): {image_in_color.shape}")
plt.imshow(image_in_color)
plt.axis('off')
plt.show()