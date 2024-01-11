#!/usr/bin/env python3

from string import punctuation


def acronyms(input_string: str) -> list:
    """Write function acronyms which takes a string as a parameter and returns
    a list of acronyms. A word is an acronym if it has length at least two, and all
    its characters are in uppercase. Before acronym detection, delete punctuation
    with the strip method."""
    results = []
    for word in input_string.split():
        cleanword = word.strip(punctuation)
        if cleanword.isupper() and len(cleanword) > 1:
            results.append(cleanword)
    return results


def main():
    print(
        acronyms(
            """For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""
        )
    )


if __name__ == "__main__":
    main()
