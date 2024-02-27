m = input("\n").replace(":)" ,"🙂" ).replace(":(","🙁")
print(m)

def main():
    m = input("\n")
    print(faces(m))

def faces(f):
    f = f.replace(":)" ,"🙂" ).replace(":(","🙁")
    return f

if __name__ == '__main__':
    main()