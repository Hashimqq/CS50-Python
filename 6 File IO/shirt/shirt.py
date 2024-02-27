import sys
from PIL import Image, ImageOps
from os.path import splitext

def main():
    check()

    try:
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = ImageOps.fit(image, size)
    photo.paste(shirt, shirt)
    photo.save(sys.argv[2])


def check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    ext1 = splitext(sys.argv[1])[1]
    ext2 = splitext(sys.argv[2])[1]
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")


if __name__ == '__main__':
    main()




