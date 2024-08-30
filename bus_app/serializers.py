from .models import Ticket, Terminal, Sale
from rest_framework.serializers import ModelSerializer


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class TerminalListSerializer(ModelSerializer):
    class Meta:
        model = Terminal
        fields = ['id',"name"]


class TerminalSerializer(ModelSerializer):
    class Meta:
        model = Terminal
        fields = "__all__"


class SaleSerializer(ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'