from django.contrib.admin import register, ModelAdmin
from .models import Wallet


@register(Wallet)
class WalletAdmin(ModelAdmin):...