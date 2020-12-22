from django.http import HttpResponse
from PIL import Image

def communism(request):
    img = Image.open("api/images/soviet.jpg")
    back = Image.open("api/images/photo.jpg")
    back = back.resize(img.size)
    blended_image = Image.blend(img, back, 0.5)
    blended_image.show()
    response = HttpResponse("dope")
    return response