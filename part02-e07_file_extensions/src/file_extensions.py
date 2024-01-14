#!/usr/bin/env python3


def file_extensions(filename):
    no_extensions = []
    extensions = {}

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            words = line.split(".")
            if len(words) == 1:
                no_extensions.extend(words)
            else:
                if words[-1] in extensions:
                    extensions[words[-1]].append(line)
                else:
                    extensions[words[-1]] = [line]
    return (no_extensions, extensions)


def main():
    results = file_extensions("filenames.txt")
    if len(results[0]):
        print(f"{len(results[0])} files with no extension")
    else:
        print("0 files with no extension")


if __name__ == "__main__":
    main()
