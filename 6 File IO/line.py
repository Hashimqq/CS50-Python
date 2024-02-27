import sys

def main():
    check()
    try:
        with open(sys.argv[1]) as file:

            p = 0
            for line in file:
                if not line.lstrip().startswith("#") and line.lstrip() != "":
                    p += 1
            print(p)

    except FileNotFoundError:
        sys.exit("file no found")

def check():
    if sys.argv[1][-3:] != ".py":
        sys.exit("not a python file")
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")



if __name__ == '__main__':
    main()
