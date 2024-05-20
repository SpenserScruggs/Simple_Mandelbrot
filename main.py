import numpy as np
import matplotlib.pyplot as plt

width = 1000
height = 1000

img = np.ones((width, height, 3))

vals = np.zeros((width, height), dtype='complex')

xlim = 1.25
ylim = 1.25
xcenter = -0.5
ycenter = 0
depth = 25

for i in range(width):
    for h in range(height):
        x = xlim * 2 * (i - width /2) / width + xcenter
        y = ylim * 2 * (h * 1j - (height/2)*1j) / height + ycenter * 1j
        vals[i][h] = x + y

old_vals = vals.copy()

for i in range(depth):
    vals = vals * vals + old_vals

angle = np.angle(vals)

def color_map(x):
    pi = np.pi

    def interp(x1, x2, y1, y2):
        nonlocal x
        return y1+(y2-y1)/(x2-x1)*(x-x1)

    if x <= -pi/3:
        color = np.array([interp(-pi, -pi/3, 1, 0), 0, interp(-pi, -pi/3, 0, 1)])
    elif x <= pi/3:
        color = np.array([0, interp(-pi/3, pi/3, 0, 1), interp(-pi/3, pi/3, 1, 0)])
    else:
        color = np.array([interp(pi/3, pi, 0, 1), interp(pi/3, pi, 1, 0), 0])

    return color


for i in range(width):
    for h in range(height):
        img[i, h] = color_map(angle[i, h]) / np.tanh(np.abs(vals[i, h]))


plt.imshow(img)
plt.axis('off')
plt.savefig("output.png", dpi=600, bbox_inches='tight', transparent=True)
plt.show()