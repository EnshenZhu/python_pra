import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# function that returns dy/dt
def model(P, t):
    # k = 1000000
    dPdt = P * (10 ** (-4) - 10 ** (-12) * P)
    return dPdt


# initial condition
p0 = 1000000

# time points
t = np.linspace(0, 20)

# solve ODE
y = odeint(model, p0, t)

# plot results
plt.plot(t, y)
plt.xlabel("month")
plt.ylabel('P')
plt.show()
