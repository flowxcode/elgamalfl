# key generation
# enc
# dec

def generate_p():
    return 13


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

