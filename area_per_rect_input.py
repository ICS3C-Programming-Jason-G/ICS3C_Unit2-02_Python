#!/usr/bin/env python3

# Created by: Jason Grace
# Created on: October 12th, 2023
# This program asks the user for the length and width of
# a rectangle in centimeters (cm). It then calculates and
# displays the area and perimeter of the rectangle.

import math


def main():
    # input
    length = int(input("Enter the length of the rectangle (cm): "))
    width = int(input("Enter the width of the rectangle (cm): "))

    # process
    area = length * width
    perimeter = 2 * (length + width)

    # output
    print("")
    print("Area = {} cm^2".format(area))
    print("Perimeter = {} cm".format(perimeter))


if __name__ == "__main__":
    main()
