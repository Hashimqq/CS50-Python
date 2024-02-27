# i = input("Input: ")
# vowels = "a,e,i,o,u,A,E,I,O,U"
# for d in vowels:
#     i = i.replace(d, "")
#
# print("Output:", i)

def main():
    i = input("Input: ")

    print("Output:", remove_vowels(i))

def remove_vowels(v):
    vowels = "a,e,i,o,u,A,E,I,O,U"
    for d in vowels:
        v = v.replace(d, "")
    return v


if __name__ == '__main__':
    main()