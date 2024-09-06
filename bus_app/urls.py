from django.urls import path
from bus_app.views import (
    welcome,
    ticket_list,
    ticket_list2,
    terminal_list,
    sale,
    new_sale,
    delete_sale,
    neshan,
    NewTicketList,
    TerminalList,
    TerminalRetrieve,
    CreateTerminal,
    DeleteTerminal,
    UpdateTerminal,
    TerminalView,
    TerminalDetails,
)


urlpatterns = [
    path("welcome", welcome),
    path("tickets", ticket_list),
    path("terminals", terminal_list),
    path("tickets/<str:input_title>", ticket_list2),
    path("sale/<str:input_name>/<str:input_phone>/<str:input_ticket>", sale),
    path("new-sale", new_sale),
    path("delete-sale/<str:sale_id>", delete_sale),
    path("neshan", neshan),
    path("ticket-list", NewTicketList.as_view()),
    path('terminal-list', TerminalList.as_view()),
    path('terminal/<int:pk>', TerminalRetrieve.as_view()),
    path('create-terminal', CreateTerminal.as_view()),
    path('delete-terminal/<int:pk>', DeleteTerminal.as_view()),
    path('update-terminal/<int:pk>', UpdateTerminal.as_view()),
    path('terminal', TerminalView.as_view()),
    path('terminal/<int:pk>', TerminalDetails.as_view()),
]
