
from __future__ import division, print_function

import sys

import numpy as np


def simulate(prob, state):

    # make new user if bathroom is unoccupied
    if not state[1]:
        state[0] = np.random.random()

    # update actual state
    state[1] = not state[1]

    # update sign state
    if state[0] < prob:
        pass
    elif state[0] < 2 * prob:
        state[2] = True
    else:
        state[2] = state[1]


if __name__ == "__main__":

    if len(sys.argv) >= 2:
        prob_co = float(sys.argv[1])
    else:
        prob_co = 1 / 3.0

    # initialize random number generator
    np.random.seed()

    # prob := probability that person totally ignores the sign
    # prob := probability that person forgets sign upon leaving
    prob = (1 - prob_co) / 2

    # (user type, actual state, sign state)
    state = [0, False, False]

    # track # of sign state count and # of times correct
    n_sign = [0, 0]
    n_valid = [0, 0]

    # simulate for "enough" times
    n_sim = int(1e6)
    for _ in range(n_sim):
        simulate(prob, state)

        n_sign[state[2]] += 1
        if state[1] == state[2]:
            n_valid[state[2]] += 1

    print("P(occ|sign_occ) = " + str(n_valid[1] / n_sign[1]))
    print("P(vac|sign_vac) = " + str(n_valid[0] / n_sign[0]))
