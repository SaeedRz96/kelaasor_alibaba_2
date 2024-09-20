from django import forms
from .models import Terminal


class TerminalForm(forms.ModelForm):
    class Meta:
        model = Terminal
        fields = ["name", "address", "open_time", "close_time"]
