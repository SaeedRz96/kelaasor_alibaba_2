from .models import Ticket, Terminal
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
