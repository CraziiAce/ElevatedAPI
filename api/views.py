from django.http import HttpResponse
from PIL import Image
from urllib.request import urlopen

def communism(request):
    url = request.GET['image_url']
    img = Image.open(urlopen(url))
    back = Image.open("api/images/photo.jpg")
    back = back.resize(img.size)
    blended_image = Image.blend(img, back, 0.5)
    blended_image.show()
    response = HttpResponse(content_type="image/jpeg")
    blended_image.save(response, "JPEG")
    return response

