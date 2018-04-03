from PIL import Image
import face_recognition

image = face_recognition.load_image_file("test.jpg")
resIma = Image.open("test.jpg")
#width, height = resIma.size
print("resolution: {} * {}".format((width, height = resIma.size) ))
#image_rect = image.get_rect()
#print("resolution: {} * {}".format(image_rect.width,image_rect.height))
face_locations = face_recognition.face_locations(image)
count = len(face_locations)
print(count)
for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    # face_image = image[top:bottom, left:right]
    # pil_image = Image.fromarray(face_image)
    # pil_image.show()
