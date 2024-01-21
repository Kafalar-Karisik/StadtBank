"""Django Module(s)"""
from django import forms


class CustomerF(forms.Form):
    """Customer From"""
    nr = forms.IntegerField(label="Customer Nr")
    amount = forms.FloatField()
