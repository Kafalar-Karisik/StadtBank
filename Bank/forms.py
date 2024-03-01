"""Django Module(s)"""
from django import forms


class CustomerF(forms.Form):
    """Customer From"""
    nr = forms.IntegerField(label="Customer Nr")
    amount = forms.FloatField()


class TransferF(forms.Form):
    """Transfer Form"""
    nr = forms.ImageField()
    type = "transfer"
    amount = forms.FloatField()
    releated_nr = forms.IntegerField()
