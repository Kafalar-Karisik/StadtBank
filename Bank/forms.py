"""Django Module(s)"""
from django import forms

from .models import Customer


class CustomerF(forms.Form):
    """Customer From"""
    nr = forms.IntegerField(label="Customer Nr")
    amount = forms.FloatField()


class TransferF(forms.Form):
    """Transfer Form"""
    nr = forms.IntegerField()
    type = "transfer"
    amount = forms.FloatField()
    related = forms.IntegerField()


class PayForm(forms.Form):
    customer = forms.ModelChoiceField(Customer.objects.all())
    type = forms.CharField()
    amount = forms.IntegerField()
