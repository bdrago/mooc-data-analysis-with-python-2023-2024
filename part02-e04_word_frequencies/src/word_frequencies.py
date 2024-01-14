#!/usr/bin/env python3


def word_frequencies(filename):
    word_counts = {}

    with open(filename, "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
    return word_counts


def main():
    pass


if __name__ == "__main__":
    main()
