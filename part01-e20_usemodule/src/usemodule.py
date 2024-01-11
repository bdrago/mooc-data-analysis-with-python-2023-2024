#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle


def main():
    # Call the functions from here
    print(triangle.hypotenuse(2.0, 2.0))
    print(triangle.area(2.0, 2.0))


if __name__ == "__main__":
    main()
