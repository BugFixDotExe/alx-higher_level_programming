#!/usr/bin/python3
for i in range(0, 100):
    if (i == 99):
        print("{:d}{:d}".format(i//10, i % 10))
        break
    print("{:d}{:d}".format(i//10, i % 10), end=", ")
