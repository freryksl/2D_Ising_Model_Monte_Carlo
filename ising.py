import numpy as np
from numba import njit

@njit
def ising_model(spins, N, I, temp, J):
    # neighbour spins
    def neighbours(spins, N, i, j):
        # periodic boundary conditions
        up = spins[i-1, j] if i > 0 else spins[N-1, j]
        down = spins[i+1, j] if i+1 < N else spins[0, j]
        left = spins[i, j-1] if j > 0 else spins[i, N-1]
        right = spins[i, j+1] if j+1 < N else spins[i, 0]
        return (up+down+left+right)
    # initial state of magnetizations array
    mag = [np.abs(np.sum(spins.copy())) / (N*N)]
    for _ in range(I):
        for f in range(N):
            for l in range(N):
                # select a random spin
                i = np.random.randint(N)
                j = np.random.randint(N)
                deltaEnergy = 2*J*spins[i,j]*neighbours(spins, N, i, j) # energy difference, if phase transition happens
                # confirm or deny phase transition according to result of conditions
                if deltaEnergy < 0 or np.random.random() < np.exp(-deltaEnergy/temp): 
                    spins[i,j] *= -1
        mag.append(np.abs(np.sum(spins.copy())) / (N*N))
    return mag

class Ising:
    def simulate(temps, N, I, J, spin_val):
        avg_mag = []
        for temp in temps:
            spins = np.random.choice([spin_val,-spin_val], size=(N,N)) # random spin configuration
            mag = ising_model(spins, N, I, temp, J) # get data of magnetizations
            avg_mag.append(np.average(mag))
        return avg_mag
    