from django.http.response import HttpResponse


def welcome_page(request):
    return HttpResponse("Welcome to Alibaba")


def train_list(request):
    my_train_list = ["Mahshad-Tehran", "Tehran-Ahvaz", "Rasht-Karaj"]
    return HttpResponse(my_train_list)


def train_detail(request, code):
    train_list = [
        {"name": "Tehran-Mashhad", "code": "1"},
        {"name": "Tehran-Tabriz", "code": "2"},
        {"name": "Tehran-Ahavaz", "code": "3"},
    ]
    for item in train_list:
        if item['code'] == code:
            return HttpResponse(item['name'])
    return HttpResponse("Train not found")
