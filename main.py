import numpy as np
from ising import Ising
from convert_time import ConvertTime as convt
import matplotlib.pyplot as plt
import time
import os

N = [5,10,25,50] # number of particles
I = [100, 1000, 10000, 1000000] # number of iterations
temps = np.arange(0.1, 5, 0.5) # temperature range
spin_val = 1 # spin value
J = 1 # interaction parameter

# create figures folder if it does not exist.
figure_path = "figures"
if not os.path.exists(figure_path): os.makedirs(figure_path)

for i in I:
    t0 = time.time()
    fig, ax = plt.subplots()
    for n in N: # simulation for each total particles
        average_magnetization = Ising.simulate(temps, n, i, J, spin_val)
        ax.plot(temps, average_magnetization, label="N: {0} x {0}".format(n))
        ax.legend()
    # elapsed time for each iteration
    dt = time.time() - t0
    # plot graph and save
    plt.title("I: {} | Periodic | s = {} | t: {}".format(i, r"$\pm 1$", convt.convert(dt)))
    plt.xlabel("kT", horizontalalignment='right', x=1.0)
    plt.ylabel(r'$\overline{M}$', rotation=0, horizontalalignment='right', y=1.0)
    plt.savefig("figures/I{}.png".format(i))