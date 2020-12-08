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

    r.recvuntil("============\n") # receive (and discard) all of the intro text including the ====
    voucher = r.recvuntil("============\n") # receive and save the ciphertext
    voucher = voucher.decode("utf-8") # we received raw bytes, interpret it as utf-8 text
    voucher = voucher.strip("\n"+"="*80+"\n") # strip the === from the ciphertext
    
    response = r.recvuntil("> ").decode("utf-8") # till input menu
    pwn.log.info("response: " + response)

    r.sendline("3") # redeem voucher
    r.sendline(voucher) # enter voucher

    r.sendline("1") # 1
    r.sendline("1")

    r.sendline("6") # 6 exit buy menue

    r.sendline("4") # exit
    response = r.recvall().decode("utf-8")
    pwn.log.info("response: " + response)

    # print(voucher)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
