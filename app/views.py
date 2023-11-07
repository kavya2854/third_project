from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jigelRani(request):
    return HttpResponse('<h1 style="background-color:cyan;"><marquee>Hai...How r u?</h1></marquee>')
