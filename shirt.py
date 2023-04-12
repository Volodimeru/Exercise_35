import sys
from PIL import Image, ImageOps

def main():
    format = (".jpg",".JPG",".jpeg",".JPEG")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(format) and sys.argv[2].endswith(".png"or".PNG" ):
        sys.exit("Input and output have different extensions")
    elif not sys.argv[1].endswith(format)  and sys.argv[2].endswith(format):
        sys.exit("Invalid input")
    else:
        try:
            shirt = Image.open("shirt.png")
            before1 = Image.open(sys.argv[1])
            resized = ImageOps.fit(before1, (600, 600))
            resized.paste(shirt, mask=shirt)
            resized.save("after.jpg")
        except FileNotFoundError:
            sys.exit("Input does not exist")

if __name__=="__main__":
    main()