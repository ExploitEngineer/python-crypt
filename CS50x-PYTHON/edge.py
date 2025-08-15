from PIL import Image, ImageFilter

before = Image.open("jjk2.jpg")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("out.jpg")
