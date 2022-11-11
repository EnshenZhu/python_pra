import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
y = [-5, -6, -7, -8, -2, -5, -6, -3, -7, -2]
z = [1, 2, 5, 3, 2, 7, 3, 3, 7, 2]

ax.scatter(x, y, z)

plt.show()
