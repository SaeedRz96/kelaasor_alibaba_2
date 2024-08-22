from django.http.response import HttpResponse, JsonResponse
from bus_app.models import Ticket, Terminal
from django.shortcuts import render


def welcome(request):
    # return HttpResponse("Welcome to Bus page")
    return render(
        request, 
        'bus_app/welcome.html'
    )


def ticket_list(request):
    tickets = Ticket.objects.all()
    my_ticket_list = []
    for item in tickets:
        ticket_dictionary = {
            "title" : item.title,
            "source" : item.source.name,
            "destination" : item.destination.name
        }
        my_ticket_list.append(ticket_dictionary)
    return JsonResponse(my_ticket_list, safe=False)


def ticket_list2(request, input_title):
    tickets = Ticket.objects.filter(title=input_title)
    my_ticket_list = []
    for item in tickets:
        ticket_dictionary = {
            "title" : item.title,
            "source" : item.source.name,
            "destination" : item.destination.name
        }
        my_ticket_list.append(ticket_dictionary)
    return JsonResponse(my_ticket_list, safe=False)


def ticket_detail(request, id):
    ticket = Ticket.objects.get(id=id)


def ticket_list3(request, input_source):
    tickets = Ticket.objects.filter(source__name=input_source)
    my_ticket_list = []
    for item in tickets:
        ticket_dictionary = {
            "title" : item.title,
            "source" : item.source.name,
            "destination" : item.destination.name
        }
        my_ticket_list.append(ticket_dictionary)
    return JsonResponse(my_ticket_list, safe=False)


def terminal_list(request):
    terminals = Terminal.objects.all()

    return render(
        request, 
        'bus_app/terminal_list.html', 
        context={'terminals':terminals}
        )