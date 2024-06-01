import numpy as np
import matplotlib.pyplot as plt


def change_vector_size(vectors):
    coeff = float(input("Enter coefficient that you want to apply: "))
    for vector in vectors:
        for i in range(len(vector)):
            vector[i] = coeff*vector[i]
    return vectors

def mirror(vectors):
    axis = input("Enter axis that you want to mirror around (enter just x or y): ")
    if axis == "x":
        for vector in vectors:
            vector[0] = -vector[0]
    if axis == "y":
        for vector in vectors:
            vector[1] = -vector[1]
    if axis == "z":
        for vector in vectors:
            vector[2] = -vector[2]
    return vectors


def rotate_axis(vectors):
    transformed_vectors = []
    axis = input("Enter axis that you want to rotate around (enter just x or y): ")
    angle = np.deg2rad(float(input("Enter angle of rotation(clockwise): ")))
    if axis == "x":
        matrix = np.array([[np.cos(angle), np.sin(angle)], [0, 1]])
    elif axis == "y":
        matrix = np.array([[1, 0], [np.sin(angle), np.cos(angle)]])
    else:
        print("Invalid axis")
    for vector in vectors:
        new_x = matrix[0][0]*vector[0] + matrix[0][1]*vector[1]
        new_y = matrix[1][0]*vector[0] + matrix[1][1]*vector[1]
        transformed_vectors.append([new_x, new_y])
    vectors = transformed_vectors
    return vectors

def rotate_figure(vectors):
    transformed_vectors = []
    angle_rad = np.deg2rad(float(input("Enter angle of rotation(clockwise): ")))
    matrix = np.array([[np.cos(angle_rad), np.sin(angle_rad)], [-np.sin(angle_rad), np.cos(angle_rad)]])
    for vector in vectors:
        new_x = matrix[0][0]*vector[0] + matrix[0][1]*vector[1]
        new_y = matrix[1][0]*vector[0] + matrix[1][1]*vector[1]
        transformed_vectors.append([new_x, new_y])
    vectors = transformed_vectors
    return vectors


def any_transformation(vectors):
    matrix_input = input("Enter matrix to transform. It should be a basis of 2 vectors.\n"
                    "Enter them in order of: x1, y1, x2, y2:\n")
    vectors_coordinates = matrix_input.split(" ")
    x1 = int(vectors_coordinates[0])
    y1 = int(vectors_coordinates[1])
    x2 = int(vectors_coordinates[2])
    y2 = int(vectors_coordinates[3])
    basis = [[x1, y1], [x2, y2]]
    transformed_vectors = []
    for vector in vectors:
        new_x = basis[0][0]*vector[0] + basis[0][1]*vector[1]
        new_y = basis[1][0]*vector[0] + basis[1][1]*vector[1]
        transformed_vectors.append([new_x, new_y])
    vectors = transformed_vectors
    return vectors
    
def print(figure):
    xpoints = np.zeros([len(figure)])
    ypoints = np.zeros([len(figure)])
    for i in range(len(figure)):
        xpoints[i] = figure[i][0]
        ypoints[i] = figure[i][1]
    plt.plot(xpoints, ypoints)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth = 0.5)
    # plt.grid()
    plt.show()
    return 0


def print_3d(figure):
    xpoints = np.zeros([len(figure)])
    ypoints = np.zeros([len(figure)])
    zpoints = np.zeros([len(figure)])
    plt.axes(projection ='3d')
    for i in range(len(figure)):
        xpoints[i] = figure[i][0]
        ypoints[i] = figure[i][1]
        zpoints[i] = figure[i][2]
    plt.plot(xpoints, ypoints, zpoints)
    plt.show()
    return 0


star = np.array([[1, 2], [2.5, 0], [4, -0.5], [2.5, -1.5], [3.5, -3.5],
                 [1, -2], [-1.5, -4], [-0.5, -1.5], [-2.8, 0], [0, 0], [1, 2]])
bird = np.array([[3, 2], [5, 1.5], [6, 2], [7, 2.5], [6, 1.5], [8, 1.5],
                 [6, 0.5], [7, 0], [6, -0.5], [5, 1], [3, 2]])
triangle_3d = np.array([(0, 2, 5), (4, 10, 3), (6, 9, 2), [0, 2, 5]])


print(triangle_3d)
print(change_vector_size(triangle_3d))
print(mirror(triangle_3d))
# ---------------------------- main part of execution -------------------------------------------------------
figure = input("Enter figure you want to transform: star or bird\n")
command = int(input("Which linear transformation you want to do?\nEnter 1 to resize\n"
                    "Enter 2 to mirror\nEnter 3 to rotate one axis\nEnter 4 to rotate whole figure\n"
                    "Enter 5 to apply custom matrix\n"))
if figure == "star":
    figure = star
elif figure == "bird":
    figure = bird
print(figure)
match command:
    case 1:
        figure = change_vector_size(figure)
    case 2:
        figure = mirror(figure)
    case 3:
        figure = rotate_axis(figure)
    case 4:
        figure = rotate_figure(figure)
    case 5:
        figure = any_transformation(figure)
print(figure)
