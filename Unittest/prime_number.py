# Write a Python unit test program to check if a given number is prime or not.
from math import sqrt


def is_prime(n):
    try:
        # ask user to input a number
        # n = int(input("Enter a number to check if its a prime number of not: "))
        # iterate from 2 to the sqrt of the number inclusive.
        # if we set the range to n, our code will spend more time running
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                print("i'm not a prime number ☹️!")
                return False
            else:
                print("Yaaay!!, you got a PRIME number handy 👯‍♂️ ")
                return True
    except:
        if n <= 0:
            raise ValueError
        if TypeError:
            raise TypeError

