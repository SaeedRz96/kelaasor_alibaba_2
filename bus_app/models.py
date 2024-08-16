from django.db import models


class Terminal(models.Model):
    name = models.CharField(max_length=500)
    address = models.TextField()
    open_time = models.TimeField()
    close_time = models.TimeField()


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    source = models.ForeignKey(
        Terminal, 
        on_delete=models.CASCADE, 
        related_name='ticket_source')
    destination = models.ForeignKey(
        Terminal, 
        on_delete=models.CASCADE,
        related_name='ticket_destinatio')
    date = models.DateField()
    time = models.TimeField()
    price = models.IntegerField()


class Sale(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT)