import numpy as np
import matplotlib.pyplot as plt

def change_vector_size(vectors):
    coeff = float(input("Enter coefficient that you want to apply: "))
    for vector in vectors:
        vector[0] = coeff*vector[0]
        vector[1] = coeff*vector[1]
    return vectors

def mirror(vectors):
    axis = input("Enter axis that you want to mirror around (enter just x or y): ")
    if axis == "x":
        for vector in vectors:
            vector[0] = -vector[0]
    if axis == "y":
        for vector in vectors:
            vector[1] = -vector[1]
    return vectors

def rotate_axis(vectors):
    axis = input("Enter axis that you want to rotate around (enter just x or y): ")
    angle = float(input("Enter angle of rotation(clockwise): "))
    if axis == "x":
        print("okay")
    if axis == "y":
        new_vector = np.array([np.cos(angle)*(-1), np.sin(angle)])
        
def rotate_figure(vectors):
    angle = float(input("Enter angle of rotation(clockwise): "))
    matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    for vector in vectors:
        vector[0] = matrix[0][0]*vector[0] + matrix[1][0]*vector[1]
        vector[1] = matrix[0][1]*vector[0] + matrix[1][1]*vector[1]
    return vectors
            
#------------------------------------------------------------------------------------------------------------------------

star = np.array([[1, 2], [2.5, 0], [4, -0.5], [2.5, -1.5], [3.5, -3.5], 
                 [1, -2], [-1.5, -4], [-0.5, -1.5], [-2.8, 0], [0, 0], [1, 2]])
bird = np.array([[3, 2], [5, 1.5], [6, 2], [7, 2.5], [6, 1.5], [8, 1.5], 
                 [6, 0.5], [7, 0], [6, -0.5], [5, 1], [3, 2]])

plt.axhline(y=0, color='r', linestyle='--')
plt.axvline(x=0, color='r', linestyle='--')



xpoints_bird = np.zeros(len(bird))
ypoints_bird = np.zeros(len(bird))
for i in range(len(bird)):
    xpoints_bird[i] = bird[i][0]
    ypoints_bird[i] = bird[i][1]
plt.plot(xpoints_bird, ypoints_bird)
# plt.grid()
# plt.show()
xpoints_star = np.zeros([len(star)])
ypoints_star = np.zeros([len(star)])
for i in range(len(star)):
    xpoints_star[i] = star[i][0]
    ypoints_star[i] = star[i][1]
plt.plot(xpoints_star,ypoints_star)
plt.grid()
plt.show()

figure = input("Enter figure you want to transform: star or bird\n")
command = int(input("Which linear transformation you want to do?\nEnter 1 to resize\n"
                    "Enter 2 to mirror\nEnter 3 to rotate one axis\n Enter 4 to rotate whole figure\n"))
if figure == "star":
    figure = star
elif figure == "bird":
    figure = bird
match command:
    case 1:
        figure = input("Enter figure you want to transform: star or bird\n")
        change_vector_size(figure)
    case 2:
        mirror(figure)
    case 3:
        rotate_axis(figure)
    case 4:
        rotate_figure(figure)