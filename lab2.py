import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
from skimage import io


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
# image_color = imread("myimage.jpg")
# 
# print(f"Висота, ширина, канали): {image_color.shape}")
# plt.imshow(image_color)
# plt.axis('off')
# plt.show()
# 
# # making it bw
# image_sum = image_color.sum(axis=2)
# image_bw = image_sum / image_color.shape[2]
# bw_height, bw_width = image_bw.shape
# print(f"Розміри чорно-білого зображення: {bw_height}, {bw_width}")
# print(f"Кількість каналів кольорів після перетворення в чорно-біле:", 1)
# 
# plt.imshow(image_bw, cmap='gray')
# plt.axis('off')
# plt.show()
# 
# # centering
# image_bw_centered = image_bw - np.mean(image_bw)
# 
# # covariance matrix
# cov_matrix = np.cov(image_bw_centered, rowvar=False)
# 
# # eigen
# eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
# # sort eigen
# sorted_index = np.argsort(eigenvalues)[::-1]
# sorted_eigenvalues = eigenvalues[sorted_index]
# sorted_eigenvectors = eigenvectors[:, sorted_index]
# 
# # finding number of components for 95% variance
# cumulative_variance = np.cumsum(sorted_eigenvalues) / np.sum(sorted_eigenvalues)
# num_components_95 = np.argmax(cumulative_variance >= 0.95)
# print(f"Number of components to cover 95% variance: {num_components_95}")
# 
# plt.plot(cumulative_variance, marker='o')
# plt.axhline(y=0.95, color='r', linestyle='--')
# plt.axvline(x=num_components_95, color='r', linestyle='--')
# plt.title('Cumulative Variance Explained by PCA Components')
# plt.xlabel('Number of Components')
# plt.ylabel('Cumulative Variance')
# plt.show()
# 
# # екфтащкьштп вфеф
# pca_components = sorted_eigenvectors[:, :num_components_95]
# image_bw_pca = np.dot(image_bw_centered, pca_components)
# 
# # reconstruction
# image_bw_reconstructed_flat = np.dot(image_bw_pca, pca_components.T)
# image_bw_reconstructed = image_bw_reconstructed_flat.reshape(image_bw.shape)
# 
# # showing diff components
# components_list = [10, 20, num_components_95, 50, 100, 500]
# 
# for i, num_components in enumerate(components_list, 1):
#     pca_components = sorted_eigenvectors[:, :num_components]
#     image_bw_pca = np.dot(image_bw_centered, pca_components)
#     image_bw_reconstructed_flat = np.dot(image_bw_pca, pca_components.T)
#     image_bw_reconstructed = image_bw_reconstructed_flat.reshape(image_bw.shape)
# 
#     plt.subplot(2, 3, i)
#     plt.imshow(image_bw_reconstructed, cmap='gray')
#     plt.title(f'{num_components} Components')
#     plt.axis('off')
# plt.show()


# ------------------------- part 3 --------------------------------------------------------
def encrypt_message(message, key_matrix):
    message_vector = np.array([ord(char) for char in message])
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))
    encrypted_vector = np.dot(diagonalized_key_matrix, message_vector)
    return encrypted_vector
def decrypt_message(encrypted_vector, key_matrix):
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))
    diagonalized_key_matrix_inv = np.linalg.inv(diagonalized_key_matrix)
    decrypted_vector = np.dot(diagonalized_key_matrix_inv, encrypted_vector)
    decrypted_message = ''.join([chr(int(round(num.real))) for num in decrypted_vector])
    return decrypted_message

# testing
message = "Hello, World!"
key_matrix = np.random.randint(0, 256, (len(message), len(message)))

encrypted_vector = encrypt_message(message, key_matrix)
print("Encrypted:", encrypted_vector)

decrypted_message = decrypt_message(encrypted_vector, key_matrix)
print("Decrypted:", decrypted_message)