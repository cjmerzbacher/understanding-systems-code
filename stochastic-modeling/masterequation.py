import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def get_m(n, mo):
    mn = mo*Sm/dm*(1/np.math.factorial(n))
    return mn

def get_g(n):
    return n*dm

def get_P(Ps, t, n, mo):
    P = Ps
    f = Sm
    if n == 0:
        dPdt = get_g(n+1)*get_m(n+1, mo) - get_m(n, mo)*(get_g(n)+f)
    else:
        dPdt = f*get_m(n-1, mo) + get_g(n+1)*get_m(n+1, mo) - get_m(n, mo)*(get_g(n)+f)
    return [dPdt]

Smdms = [0.25, 0.5, 0.75, 1., 1.25, 1.5, 1.75, 2., 3.]

Smdm = 0.01
Sm = Smdm*1
dm = 1/Smdm
max_n = 10 #number of mRNA molecules to simulate having
n = np.arange(max_n)
g = [get_g(i) for i in n]
times = np.linspace(0., 1., 101)

Ps = []
for mo in np.arange(0., max_n, 1.): #iterate on mo
    for i in n:
        m = [get_m(i,mo) for i in n]
        ans = odeint(func=get_P, y0=[mo], t=times, args=(i,mo))
        Ps.append(ans[:, 0])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True)
for i in np.arange(0, len(Ps), 1):
    ax1.plot(times, Ps[i], color='k')
ax1.set_xlabel('Time (t/tmax)')
ax1.set_ylabel('Number of mRNA molecules')
ax1.set_ylim([0, 10])
ax1.grid()

#Pull final values for histogram construction
hist = [P[-1] for P in Ps]


ax2.hist(hist, bins=max_n, density=True)
ax2.set_xlabel('Number of mRNA molecules')
ax2.set_ylabel('Proportion of trajectories')