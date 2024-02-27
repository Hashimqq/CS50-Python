def main():
    i = input("Input: ")
    print("Output:", shorten(i))

def shorten(word):

    vowels = "a,e,i,o,u,A,E,I,O,U"
    for d in vowels:
        word = word.replace(d, "")
    return word

if __name__ == "__main__":
    main()