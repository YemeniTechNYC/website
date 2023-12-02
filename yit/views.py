from django.http import HttpResponse
from django.shortcuts import render


def health(request):
    return HttpResponse("OK", status=200)


def index(request):
    return render(request, "yit/index.html")
