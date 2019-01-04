# Lab11-Primes-APR.py
# Amanda Ramos
# A program to determine if a number is prime.

import math
def prime(num):
    keepgoing = True
    prime = True 
    factor = 2 
    while keepgoing and (int(num) > 0):
        if int(num) % factor == 0:
            keepgoing = True
            prime = False
            print(num,"is not a prime number")
            factor = factor + 1
        elif int(num) % factor == 0:
            print(num,"is not a prime number")
            prime = False
            keepgoing = True
        else:
            if factor >= int(math.sqrt(int(num))):
               prime = True
               keepgoing = True
               print(num,"is a prime number")
            else:
                prime = False
                keepgoing = True
        num = input("Enter a positive integer, or a non-positive value to quit:" )

# end prime


def main():
    testnum = input("Enter a positive integer, or a non-positive value to quit:" )
    prime(testnum)

# end main
main()
