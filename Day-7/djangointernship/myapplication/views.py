from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return HttpResponse("<h1>Hello World!!</h1>")

def aboutpageview(request):
    return HttpResponse("This is about us page")
    