import re


def main():
    print(count(input("Text: ")))


def count(s):
    x = 0
    email = re.findall(r'\bum\b', s.lstrip().lower())
    for i in email:
        if i == "um":
            x += 1
    return x


if __name__ == "__main__":
    main()




