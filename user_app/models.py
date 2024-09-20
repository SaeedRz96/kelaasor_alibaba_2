from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField(default=0)


class RequestLog(models.Model):
    method = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    ip_address = models.GenericIPAddressField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
