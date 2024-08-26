from django.urls import path
from bus_app.views import welcome, ticket_list, ticket_list2, terminal_list, sale, new_sale, delete_sale


urlpatterns = [
    path("welcome", welcome),
    path("tickets", ticket_list),
    path("terminals", terminal_list),
    path("tickets/<str:input_title>", ticket_list2),
    path("sale/<str:input_name>/<str:input_phone>/<str:input_ticket>", sale),
    path("new-sale", new_sale),
    path('delete-sale/<str:sale_id>', delete_sale)
]
