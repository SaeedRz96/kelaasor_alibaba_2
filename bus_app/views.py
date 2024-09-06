from django.http.response import HttpResponse, JsonResponse, HttpResponseBadRequest
from bus_app.models import Ticket, Terminal, Sale
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from .serializers import TicketSerializer, TerminalSerializer, TerminalListSerializer
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .tasks import send_email_to_customer


def welcome(request):
    # return HttpResponse("Welcome to Bus page")
    return render(request, "bus_app/welcome.html")


def ticket_list(request):
    tickets = Ticket.objects.all()
    my_ticket_list = []
    for item in tickets:
        ticket_dictionary = {
            "ID": item.id,
            "title": item.title,
            "source": item.source.name,
            "destination": item.destination.name,
        }
        my_ticket_list.append(ticket_dictionary)
    return JsonResponse(my_ticket_list, safe=False)


def ticket_list2(request, input_title):
    tickets = Ticket.objects.filter(title=input_title)
    my_ticket_list = []
    for item in tickets:
        ticket_dictionary = {
            "title": item.title,
            "source": item.source.name,
            "destination": item.destination.name,
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
            "title": item.title,
            "source": item.source.name,
            "destination": item.destination.name,
        }
        my_ticket_list.append(ticket_dictionary)
    return JsonResponse(my_ticket_list, safe=False)


def terminal_list(request):
    terminals = Terminal.objects.all()

    return render(
        request, "bus_app/terminal_list.html", context={"terminals": terminals}
    )


def sale(request, input_name, input_phone, input_ticket):
    selected_ticket = Ticket.objects.get(id=input_ticket)
    if selected_ticket.capacity == 0:
        return HttpResponse("No Capacity")
    new_sale = Sale.objects.create(
        name=input_name, phone=input_phone, ticket=selected_ticket
    )
    selected_ticket.capacity -= 1
    selected_ticket.save()
    # send email to customer
    send_email_to_customer.delay("customer_email")
    return HttpResponse("new ticket with name: {}".format(new_sale.name))


@csrf_exempt
def new_sale(request):
    if request.method == "POST":
        body = json.loads(request.body)
        selected_ticket = Ticket.objects.get(id=body["input_ticket"])
        if selected_ticket.capacity == 0:
            return HttpResponse("No Capacity")
        Sale.objects.create(
            name=body["input_name"], phone=body["input_phone"], ticket=selected_ticket
        )
        selected_ticket.capacity -= 1
        selected_ticket.save()
        return HttpResponse("new ticket reserved")
    else:
        return HttpResponse("BAD REQUEST")


@csrf_exempt
def delete_sale(request, sale_id):
    if request.method == "DELETE":
        Sale.objects.get(id=sale_id).delete()
        return HttpResponse("Sale Deleted")
    else:
        return HttpResponse("Bad Request")


def neshan(request):
    url = "https://api.neshan.org/v4/direction?type=car&origin=35.7052111,51.3350869&destination=35.7668379,51.3554544"
    api_key = "service.2f93c88dfc154d7bb5af4c160c4faa09"
    response = requests.get(url, headers={"Api-Key": api_key})
    return JsonResponse(
        json.loads(response.content)["routes"][0]["legs"][0]["summary"], safe=False
    )


class NewTicketList(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["price", "capacity"]
    search_fields = ["title"]
    filterset_fields = ['source',"destination"]


class TerminalList(ListAPIView):
    queryset = Terminal.objects.all()
    serializer_class = TerminalListSerializer


class TerminalRetrieve(RetrieveAPIView):
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer


class CreateTerminal(CreateAPIView):
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer


class DeleteTerminal(DestroyAPIView):
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer


class UpdateTerminal(UpdateAPIView):
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer


class TerminalView(ListCreateAPIView):
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        elif self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        return super(TerminalView, self).get_permissions()


class TerminalDetails(RetrieveUpdateDestroyAPIView):
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer
