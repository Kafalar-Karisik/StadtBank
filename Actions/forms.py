from django import forms

class CustomerF(forms.Form):
    nr = forms.IntegerField(label="Customer Nr")
    amount = forms.FloatField()
