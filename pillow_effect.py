from PIL import Image
from PIL import ImageFilter

# merge two image
flower = Image.open("flower.jpg")
girl = Image.open("girl.jpg")

r1, g1, b1 = flower.split()
r2, g2, b2 = girl.split()

new_img= Image.merge("RGB",(r2, g1, b2))
new_img.show()


# basic transformation like  resize, flip

bear = Image.open("bear.gif")
new_bear = bear.resize((250,250))
flip_bear = bear.transpose(Image.FLIP_TOP_BOTTOM)
spin_bear=bear.transpose(Image.ROTATE_90)
new_bear.show();
flip_bear.show();
spin_bear.show();


# Modes and Filters

old_girl=Image.open("girl.jpg")
black_white_girl = old_girl.convert("L")
black_white_girl.show()

blur_girl=old_girl.filter(ImageFilter.BLUR)
blur_girl.show()

detail_girl=old_girl.filter(ImageFilter.DETAIL)
edges_girl=old_girl.filter(ImageFilter.FIND_EDGES)

detail_girl.show()
edges_girl.show()