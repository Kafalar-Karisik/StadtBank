"""Django Module(s)"""
from django import forms

from .models import Customer


class CustomerF(forms.Form):
    """Customer From"""
    nr = forms.IntegerField(label="Customer Nr")
    amount = forms.FloatField()


class TransferF(forms.Form):
    """Transfer Form"""
    nr = forms.ModelChoiceField(Customer.objects.all())
    type = "transfer"
    amount = forms.FloatField()
    related = forms.ModelChoiceField(Customer.objects.all())


class PayF(forms.Form):
    """Pay Form"""
    customer = forms.ModelChoiceField(Customer.objects.all())
    payType = forms.CharField()
    payAmount = forms.IntegerField()
    isSalary = forms.CheckboxInput()


class CreditF(forms.Form):
    """Credit Form"""
    customer = forms.ModelChoiceField(Customer.objects.all())
    amount = forms.IntegerField()


class newCustomerF(forms.Form):
    """New Customer Form"""
    name = forms.CharField()
