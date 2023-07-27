from django import forms

class CustomerF(forms.Form):
    nr = forms.IntegerField(label="Customer Nr")
    ammount = forms.FloatField()
