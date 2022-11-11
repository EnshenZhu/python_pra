import math

xyz = [[1, 0, 0],
       [0, 1, 0],
       [0, 0, 1]]

radius = (xyz[0][0] ** 2
        + xyz[0][1] ** 2
        + xyz[0][2] ** 2
        + xyz[1][0] ** 2
        + xyz[1][1] ** 2
        + xyz[1][2] ** 2
        + xyz[2][0] ** 2
        + xyz[2][1] ** 2
        + xyz[2][2] ** 2) ** 0.5

print(radius)

phi = math.atan((xyz[0][1] + xyz[1][1] + xyz[2][1])
                  / (xyz[0][0] + xyz[1][0] + xyz[2][0]))

print('phi =', phi)