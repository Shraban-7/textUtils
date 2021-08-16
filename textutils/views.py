# This file create by me 

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Shraban")

def about(request):
    return HttpResponse("About Shraban")
    