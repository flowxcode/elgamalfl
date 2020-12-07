"""Console script for elgamalfl."""
import argparse
from elgamalfl import ElKey
import sys

from pwn import *

def main():
    """Console script for elgamalfl."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    # print("Replace this message by putting your code into "
    #       "elgamalfl.cli.main")



    r = remote("webshop2.chals.fuzzy.land", 5209) # connect to the service
    r.recvuntil("============\n") # receive (and discard) all of the intro text including the ====
    text = r.recvuntil("============\n") # receive and save the ciphertext
    text = text.decode("utf-8") # we received raw bytes, interpret it as utf-8 text
    text = text.strip("\n"+"="*80+"\n") # strip the === from the ciphertext

    # recover the key
    recovered_key = guess_key(text)
    log.info("Keyguess = " + recovered_key)

    r.recvuntil("text:\n") # receive the rest of the prompt (one could also use r.recvline() multiple times)
    r.sendline(recovered_key) # send our recovered key

    response = r.recvall().decode("utf-8") # get all of the remaining response (this reads until server shuts down)
    log.info("Server response: " + response) # log the response on the console







    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
