import numpy as np
import math
from matplotlib import pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Slider
saturation = widgets.IntSlider(min=1., max=60.)
print("Saturation strength: ")
display(saturation)

# Constants
r = 0.5 # intrinsic growth rate
K = 800 # carrying capacity
h = 25
A = saturation.value

# Plot fishery phase portrait (with saturation term)

def fishery_model(n):
    return r*n*(1-(n/K))-h*n/(A+n)

pops = np.linspace(0., (5*K)/4, num = 3*K)

# zeros calculated in wolfram alpha
zeros = [0]
fold = (A+K)**2 - 4*h*K/r
# cut out zeros that aren't real
if fold > 0:
    zeros.append(0.5 * (K - A - math.sqrt(fold)))
    zeros.append(0.5 * (K - A + math.sqrt(fold)))
elif fold == 0:
    zeros.append(K - A)
    
print(zeros)

# Plot phase portrait
fig = plt.figure()
ax = plt.axes(xlim=(0,1.25*K), ylim=(-0.25*r*K,0.3*r*K))
plt.plot(pops, fishery_model(pops))

# Mark fixed points
for fixed_point in zeros:
    if fixed_point >=0:
        plt.plot(fixed_point,0,'go')
            

# Turn on the grid
plt.plot([0,5*K/4], [0,0], 'r-')
ax.grid()
plt.xlabel("Stock")
plt.ylabel("Growth")

plt.show()