#!/usr/bin/python3
for i in range(-122, -96):
    i = i * -1
    if i % 2 != 0:
        i = i - 32
    print("{:s}".format(chr(i)), end="")
