# key generation
# enc
# dec

import sys

from sage.all import *

def generate_p():
    smoothest = 2^30 # just something large
    for p in primes(2^24, 2^25):
        smoothness = 0
        for f, e in (p - 1).factor():
            if e != 1:
                smoothness = 2^30
                break
            smoothness += f
        if smoothness < smoothest:
            smooth = p
            smoothest = smoothness
        print(smooth, smooth - 1, (smooth - 1).factor())

    p = sagemath.random_prime(2^8-1, False, 2^7)
    return p


def generate_g():
    return 2


def generate_x():
    return 1


def calc_h():
    return 4


class ElKey:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each spec par

        self.p = generate_p()
        self.g = generate_g()
        self.h = calc_h()
        self.x = generate_x()

    def add_trick(self, trick):
        self.tricks.append(trick)


def main():
   

    key = ElKey("testname")

    # generate properties for elgamal
    print(key)
    print(vars(key))




    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
