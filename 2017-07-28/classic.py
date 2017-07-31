
from __future__ import print_function

import math
import sys
import timeit


def divs_and_mults(num, maxval):

    valid = set()

    # compute divisors
    mid = math.ceil(math.sqrt(num))
    for n in range(1, int(mid) + 1):
        if num % n == 0:
            valid.add(n)
            div = num / n
            if div != n:
                valid.add(div)
            
    # compute multiples
    mult = 2 * num
    while mult <= maxval:
        valid.add(mult)
        mult += num

    return valid


def longest_chain(maxval):

    # compute valid "next" links for all values
    valid = {}
    for n in range(1, maxval + 1):
        valid[n] = divs_and_mults(n, maxval)

    # maintain a stack to store "recursive" data
    longest = []
    chain = []
    stack = []

    links = range(maxval, 0, -1)
    while True:

        # last set of links was exhausted, back up and try again
        if not links:
            if len(chain) > len(longest):
                longest = list(chain)
            if len(chain) == 0:
                break
            chain.pop()
            links = stack.pop()

        # add new link to chain
        else:
            chain.append(links.pop())
            stack.append(links)
            links = valid[chain[-1]] - set(chain)

    return longest


if __name__ == "__main__":

    if len(sys.argv) >= 2:
        maxval = int(sys.argv[1])
    else:
        maxval = 100

    assert maxval > 1, "invalid maximum value"

    chain = longest_chain(maxval)
    print("Found chain of length {0}.".format(len(chain)))
    print(chain)
