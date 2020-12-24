from django.http import HttpResponse
from PIL import Image
from urllib.request import urlopen
from django.http.response import JsonResponse
import praw


def communism(request):
    url = request.GET["image_url"]
    img = Image.open(urlopen(url))
    back = Image.open("api/images/soviet.jpg")
    back = back.resize(img.size)
    blended_image = Image.blend(img, back, 0.5)
    response = HttpResponse(content_type="image/jpeg")
    blended_image.save(response, "JPEG")
    return response


def meme(request):
    return JsonResponse({"msg": "still WIP"})
