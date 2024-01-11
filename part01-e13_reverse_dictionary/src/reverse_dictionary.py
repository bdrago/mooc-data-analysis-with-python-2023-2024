#!/usr/bin/env python3


def reverse_dictionary(english_dict: dict) -> dict:
    finnish_dict = {}

    for eng_word, fin_words in english_dict.items():
        for word in fin_words:
            if word in finnish_dict:
                finnish_dict[word].append(eng_word)
            else:
                finnish_dict[word] = [eng_word]

    return finnish_dict


def main():
    d = {
        "move": ["liikuttaa"],
        "hide": ["piilottaa", "salata"],
        "six": ["kuusi"],
        "fir": ["kuusi"],
    }
    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()
