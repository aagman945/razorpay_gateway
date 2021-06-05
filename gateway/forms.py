from django import forms
from .models import payments

class paymentForm(forms.ModelForm):
    
    class Meta:
        model = payments
        fields = ("amount",)
