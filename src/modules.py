from PIL import Image


def imgDimensions(imgName):
    img = Image.open(imgName)
    return {"width": img.size[0], "height": img.size[1]}


def imgPixels(imgName):
    with open(imgName) as file:
        lines = file.readlines()

    allPixels = ""

    for line in lines:
        line = line.strip()
        if line.isdigit():
            allPixels += line

    return allPixels


def printImage(pixels, dimensions):
    for i, p in enumerate(pixels):
        if i != 0 and (i + 1) % dimensions["width"] == 0:
            print(p, end="\n")
        else:
            print(p, end="")
