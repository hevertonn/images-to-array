import modules as m

imageName = "myImage.pbm"

px = m.imgPixels(imageName)
dimensions = m.imgDimensions(imageName)

m.printImage(px, dimensions)
