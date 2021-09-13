#!/usr/bin/env python3

# Created by: Rodas
# Created on: Sep 2021
# This program calculates the area and circumference of a circle
#    with radius 15mm

import math


def main():
    # this function calculates the area and circumference

    print("If a circle has a radius of 15mm: ")
    print("")
    print("Area is {} mm².".format(math.pi * 15 ** 2))
    print("Circumference is {} mm.".format(2 * math.pi * 15))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
