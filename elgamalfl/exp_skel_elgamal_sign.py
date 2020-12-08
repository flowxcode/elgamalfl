"""Console script for elgamalfl."""
import argparse
from elgamalfl import ElKey
import sys

# from pwn import *
import pwn

def main():
    r = pwn.remote("webshop2.chals.fuzzy.land", 5209) # connect to the service
    
    response = r.recvuntil("Name: ").decode("utf-8") # input
    pwn.log.info("response: " + response)
    r.sendline("snahx")

    print("logged on")
    
    response = r.recvuntil("> ").decode("utf-8") # till input menu
    pwn.log.info("response: " + response)

    r.sendline("4")

    response = r.recvall().decode("utf-8")
    pwn.log.info("response: " + response)

    # text = r.recvuntil("============\n") # receive and save the ciphertext
    # text = text.decode("utf-8") # we received raw bytes, interpret it as utf-8 text
    # text = text.strip("\n"+"="*80+"\n") # strip the === from the ciphertext








    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
