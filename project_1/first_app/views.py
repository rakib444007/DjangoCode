from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def about(request):
    return HttpResponse("This is about page.")

def courses(request):

    return HttpResponse("This is courses page.")


def Home(request):

    return HttpResponse("This is first home page.")