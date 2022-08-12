import sys, os
from PIL import Image, ImageOps

def main():
    path = command_argument()
    images(path[0], path[1])

# verified command line input
def command_argument():
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few argument")

    path1 = os.path.splitext(sys.argv[2])
    path2 = os.path.splitext(sys.argv[2])


    if path1[1] not in ('.png', '.jpg', '.jpeg'):
        sys.exit("not expected image file")
    elif path1[1] != path2[1]:
        sys.exit("input and output have different extension")
    return (sys.argv[1], sys.argv[2])

# resize, crop and paste an image
def images(path1, path2):
    image1 = Image.open(path1)
    shirt = Image.open(path2)
    size = shirt.size
    image2 = ImageOps.fit(image1, size)
    shirt.paste(image1)
    shirt.save('constume.png')
    


if __name__ == "__main__":
    main()


        
    


