from django.db import models
from django.contrib.auth.models import User


class Terminal(models.Model):
    name = models.CharField(
        max_length=500,
        verbose_name="Terminal Name",
        help_text="The terminal name should be less than 500 character",
    )
    address = models.TextField()
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "My Terminal"
        verbose_name_plural = "My Terminal"


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    source = models.ForeignKey(
        Terminal, on_delete=models.CASCADE, related_name="ticket_source"
    )
    destination = models.ForeignKey(
        Terminal, on_delete=models.CASCADE, related_name="ticket_destinatio"
    )
    date = models.DateField()
    time = models.TimeField()
    price = models.IntegerField()
    capacity = models.IntegerField(default=10)


class Sale(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT)
