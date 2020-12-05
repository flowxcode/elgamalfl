# key generation
# enc
# dec

import sys

import random 
from math import pow
from math import gcd

# ------------------------------------------------------------------ #
# helper
def cust_gcd(a, b):
    print("custom gcd")
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)
# ------------------------------------------------------------------ #


# prime number
def generate_p():
	key = random.randint(pow(10, 10), pow(10, 20)) # randint between 10tothe10 and 20
	return key


def generate_g(p):
    key = random.randint(pow(10, 10), pow(10, 20)) # randint between 10tothe10 and 20
    while gcd(p, key) != 1:
        key = random.randint(pow(10, 20), q)
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
        self.g = generate_g(self.p)
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
