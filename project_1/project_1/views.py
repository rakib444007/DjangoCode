# from django.http import HttpResponse

# def contact(request):
#     return HttpResponse("this is contact page")

# def home(request):
#     return HttpResponse("this is home page")

from django.http import HttpResponse

def contact(request):
    return HttpResponse("This is contact page")


def Home(request):
    return HttpResponse("This is home page")