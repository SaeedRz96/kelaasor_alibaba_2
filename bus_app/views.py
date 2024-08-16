from django.http.response import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to Bus page")