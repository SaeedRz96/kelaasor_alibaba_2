from django.urls import path
from bus_app.views import welcome, ticket_list, ticket_list2, terminal_list


urlpatterns = [
    path('welcome', welcome),
    path('tickets', ticket_list),
    path('terminals', terminal_list),
    path('tickets/<str:input_title>', ticket_list2)
] 