from django.contrib.admin import register, ModelAdmin
from bus_app.models import Terminal, Ticket, Sale


@register(Terminal)
class TerminalAdmin(ModelAdmin):
    pass 


@register(Ticket)
class TicketAdmin(ModelAdmin):
    pass 


@register(Sale)
class SaleAdmin(ModelAdmin):
    pass 