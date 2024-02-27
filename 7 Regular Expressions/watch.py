import re

def main():
    print(parse(input("HTML: ")))


def parse(s):

    # get = re.search(r'src="(.+?)"', s)
    # if get:
    #     s = get.group(1)
    #     return f"{s}"


    match = re.search(r'src="([^"]*)"', s, re.IGNORECASE)


    if match:
        s = match.group(1)
        s = re.sub('http:', 'https:', s)
        return s.replace("www.","").replace("com/embed","be").replace("youtube","youtu").lstrip()

if __name__ == "__main__":
    main()




