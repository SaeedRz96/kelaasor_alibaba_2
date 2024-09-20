from django.contrib.admin import register, ModelAdmin
from .models import Wallet, RequestLog


@register(Wallet)
class WalletAdmin(ModelAdmin):...

@register(RequestLog)
class RequestLogAdmin(ModelAdmin):...