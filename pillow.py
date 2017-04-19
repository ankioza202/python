from PIL import Image

img=Image.open("flower.jpg")
print(img.size)
print(img.format)
img.show()

# crop the image

area=(100,100,400,500)
cropped_img=img.crop(area)
cropped_img.show()

# combine two image
flower=Image.open("flower.jpg")
bear=Image.open("bear.gif")
combineArea=(100,100,500,500)
flower.paste(bear)
flower.show()

# getting individual channel color
img1=Image.open("flower.jpg")
r,g,b=img1.split()
r.show()
g.show()
b.show()
