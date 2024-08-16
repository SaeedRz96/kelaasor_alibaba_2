from django.contrib.admin import register, ModelAdmin
from bus_app.models import Terminal, Ticket, Sale


@register(Terminal)
class TerminalAdmin(ModelAdmin):
    list_display = [
        'name',
        'open_time',
        'close_time'
    ]
    search_fields = [
        'name'
    ]


@register(Ticket)
class TicketAdmin(ModelAdmin):
    list_display = [
        'title',
        'source',
        'destination',
        'date',
        'time'
    ] 
    search_fields = [
        'title'
    ]
    list_filter = [
        'date',
        'source',
    ]


@register(Sale)
class SaleAdmin(ModelAdmin):
    pass 