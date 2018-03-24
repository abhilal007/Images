from PIL import Image

image = Image.open("")#fill "" with the image location or name
size = width, height = image.size

dummy = image.resize((160, 300), Image.LANCZOS)
dummy.save("test2.jpg", quality = 95)

