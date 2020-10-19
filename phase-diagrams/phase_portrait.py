import numpy as np
from math import exp
from matplotlib import pyplot as plt
import ipywidgets as widgets
from IPython.display import 

# Sliders
growth = widgets.FloatSlider(min=0.1, max=0.8)
carrying = widgets.IntSlider(min=10., max = 1000.)
print("Growth rate: ")
display(growth)
print("Carrying Capacity: ")
display(carrying)

# Constants
r = growth.value  # growth rate
K = carrying.value  # carrying capacity

def phase_portrait(pops):
    n_dot = []
    for n in pops:
        n_dot.append(r*n*(1-(n/K)))
    return n_dot

pops = np.linspace(0., (5*K)/4)

# Plot phase portrait
fig = plt.figure()
ax = plt.axes(xlim=(0,1.25*K), ylim=(-0.25*r*K,0.3*r*K))
plt.plot(pops, phase_portrait(pops))

# Plot trajectories
plt.arrow(0,0,K,0,length_includes_head=True,color='red',head_width=0.02,head_length=0.3)
plt.arrow(1.25*K,0,-0.25*K,0,length_includes_head=True,color='red',head_width=0.02,head_length=0.3)

# Plot fixed points
plt.plot(0,0,'go')
plt.plot(K,0,'go')

# Turn on the grid
ax.grid()
plt.xlabel("Stock")
plt.ylabel("Growth")

plt.show()