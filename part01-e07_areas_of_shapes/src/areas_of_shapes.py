#!/usr/bin/env python3

import math


def area_triangle(base: float, height: float) -> float:
    return (base * height) / 2


def area_rectangle(length: float, width: float) -> float:
    return length * width


def area_circle(radius: float) -> float:
    return math.pi * radius**2


def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "triangle":
            base = float(input("Give base of the triangle:: "))
            height = float(input("Give height of the triangle: "))
            print(f"The area is {area_triangle(base, height):.6f}")
        elif shape == "rectangle":
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            print(f"The area is {area_rectangle(length, width):.6f}")
        elif shape == "circle":
            radius = float(input("Enter the radius: "))
            print(f"The area is {area_circle(radius):.6f}")
        elif shape == "":
            break
        else:
            print("Unknown shape!")
            continue


if __name__ == "__main__":
    main()
