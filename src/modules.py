from PIL import Image
import sys


def dimensionsAndPixels(imgName):
    with Image.open(imgName) as img:
        dimensions = {"width": img.size[0], "height": img.size[1]}

    with open(imgName) as file:
        lines = file.readlines()

    pixels = ""

    for line in lines:
        line = line.strip()
        if line.isdigit():
            pixels += line

    if dimensions["width"] * dimensions["height"] == len(pixels):
        return (dimensions, pixels)

    print("A imagem é inválida!!!")
    sys.exit(1)


def printImage(dimensions, pixels):
    for i, p in enumerate(pixels):
        if i != 0 and (i + 1) % dimensions["width"] == 0:
            print(p, end="\n")
        else:
            print(p, end="")
