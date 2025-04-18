import modules as m

imageName = "images/teste.pbm"

(dim, px) = m.dimensionsAndPixels(imageName)

m.printImage(dim, px)

print(m.createNpArray(dim, px))
