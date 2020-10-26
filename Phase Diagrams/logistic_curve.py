import numpy as np
from math import exp
from matplotlib import pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Sliders
growth = widgets.FloatSlider(min=0.1, max=0.8)
carrying = widgets.IntSlider(min=10., max = 1000.)
initial = widgets.IntSlider(min=5., max = 1200.)
print("Growth rate: ")
display(growth)
print("Carrying Capacity: ")
display(carrying)
print("Initial population: ")
display(initial)

# Constants
r = growth.value  # growth rate
K = carrying.value  # carrying capacity
n_zero = initial.value  # population at t=0
A = (K-n_zero)/n_zero

# Plot logistic time series

def logistic(times):
    n = []
    for t in times:
        n.append(K/(1+(K-n_zero)/n_zero*exp(-r*t)))
    return n

t = np.linspace(0., 40)

# Set constants
r = 0.4; K = 700

# One time series for each initial value
n_zero = 100
logistic_a = logistic(t)

n_zero = 800
logistic_b = logistic(t)

n_zero = K
logistic_c = logistic(t)

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True, sharex=True)
axs[0].plot(t, logistic_a)
axs[0].set_xlim([0,20])
axs[0].plot(t, [K]*50, 'r--')
axs[1].plot(t, logistic_b)
axs[1].plot(t, [K]*50, 'r--')
axs[2].plot(t, logistic_c)
axs[2].plot(t, [K]*50, 'r--', Label='K')

plt.legend()
axs[1].set_xlabel('time, year')
axs[0].set_ylabel('Fish Stock')

fig.suptitle("Demonstration of the Logistic Model")

plt.show()