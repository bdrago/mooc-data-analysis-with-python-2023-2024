#!/usr/bin/env python3

import re


def integers_in_brackets(s):
    results = re.findall(r"\[\s*([+-]?\d+)\s*\]", s)
    return [int(num) for num in results]


def main():
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"))


if __name__ == "__main__":
    main()
