#!/usr/bin/env python3


class Rational:
    def __init__(self, numerator: int, denominator: int) -> None:
        self.num = numerator
        self.den = denominator

    def __str__(self) -> str:
        return f"Rational({self.num},{self.den})"

    def __add__(self, rational2: "Rational") -> "Rational":
        new_numerator = (self.num * rational2.den) + (rational2.num * self.den)
        new_denominator = self.den * rational2.den
        return Rational(new_numerator, new_denominator)

    def __mul__(self, rational2: "Rational") -> "Rational":
        new_numerator = self.num * rational2.num
        new_denominator = self.den * rational2.den
        return Rational(new_numerator, new_denominator)

    def __sub__(self, rational2: "Rational") -> "Rational":
        new_numerator = (self.num * rational2.den) - (rational2.num * self.den)
        new_denominator = self.den * rational2.den
        return Rational(new_numerator, new_denominator)

    def __truediv__(self, rational2: "Rational") -> "Rational":
        new_numerator = self.num * rational2.den
        new_denominator = self.den * rational2.num
        return Rational(new_numerator, new_denominator)

    def __eq__(self, rational2: "Rational") -> bool:
        return self.num * rational2.den == rational2.num * self.den

    def __lt__(self, rational2: "Rational") -> bool:
        return self.num * rational2.den < rational2.num * self.den

    def __gt__(self, rational2: "Rational") -> bool:
        return self.num * rational2.den > rational2.num * self.den


def main():
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)
    print(r1)
    print(r2)
    print(r1 * r2)
    print(r1 / r2)
    print(r1 + r2)
    print(r1 - r2)
    print(Rational(1, 2) == Rational(2, 4))
    print(Rational(1, 2) > Rational(2, 4))
    print(Rational(1, 2) < Rational(2, 4))


if __name__ == "__main__":
    main()
