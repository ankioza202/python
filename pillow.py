from PIL import Image

img=Image.open("flower.jpg")

print(img.size)

print(img.format)

img.show()
