"""Console script for elgamalfl."""
import argparse
from elgamalfl import ElKey
import sys


def main():
    """Console script for elgamalfl."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    # print("Replace this message by putting your code into "
    #       "elgamalfl.cli.main")


    key = ElKey("testname")

    # generate properties for elgamal
    print(key)
    print(vars(key))








    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
