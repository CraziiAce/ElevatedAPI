from django.shortcuts import redirect, render
from django.conf import settings
from tokenlib import make_token
from pymongo import MongoClient

mcl = MongoClient()
data = mcl.ElevatedAPI.tokens


def dash(request):
    return render(request, "dash/index.html")


def apply(request):
    secret = settings.TOKEN_SECRET

    token = make_token({"userid": user_id}, secret=secret)