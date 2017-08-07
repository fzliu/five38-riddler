
from __future__ import division, print_function

from multiprocessing import Pool
import sys

import numpy as np


def simulate(n_kids):

    # create array to track kids + teacher
    had_potato = np.zeros(n_kids + 1, dtype=np.bool)
    pos = n_kids / 2

    # move the position by either -1 or 1 until complete
    while np.sum(had_potato) < n_kids:
        had_potato[pos] = True
        pos += np.random.randint(2) * 2 - 1
        pos %= had_potato.size

    return np.argmin(had_potato)


if __name__ == "__main__":

    if len(sys.argv) >= 2:
        n_kids = int(sys.argv[1])
    else:
        n_kids = 30

    # initialize random number generator
    np.random.seed()

    # simulate for "enough" times
    n_sim = int(1e6)
    pool = Pool(processes=8)
    winners = pool.map(simulate, [n_kids] * n_sim)
    probs = np.bincount(winners) / float(n_sim)

    print("Win probabilities")
    print(probs)
