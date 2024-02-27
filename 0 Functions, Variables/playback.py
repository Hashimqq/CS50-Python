p = input("\n").replace(" " , "...")
print(p)


def main():
    p = input("\n").lower()
    print(playback(p))


def playback(p):
    p = p.replace(" " , "...")
    return p


if __name__ == '__main__':
    main()