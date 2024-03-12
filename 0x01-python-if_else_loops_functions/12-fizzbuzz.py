#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0:
            print("{:s}".format("Fizz"), end=" ")
        elif n % 5 == 0:
            print("{:s}".format("Buzz", end=" "))
        elif n % 3 == 0 and n % 5 == 0:
            print("{:s}".format("FizzBuzz"), end=" ")
        else:
            print("{:d}".format(n), end=" ")
