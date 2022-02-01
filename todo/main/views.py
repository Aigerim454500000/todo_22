from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")

def check(request):
    return HttpResponse("test 2 page")