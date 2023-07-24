from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Actions.models import Customer, Action
from django.http import Http404

# Create your views here.
def index(request):
    customers = Customer.objects.all()
    actions = Action.objects.all()
    return render(request, 'dashboard.html', {'customers': customers, 'actions': actions})


class Actions(View):
    def get(self, request):
        transaktionen = Action.objects.all()
        return render(request, 'actions.html', {'actions': transaktionen})


class Customers(View):
    def get(self, request):
        kunden = Customer.objects.all()
        return render(request, 'customers.html', {'customers': kunden})


class DetailView(View):
    """ID, Numer, Datum, Type, Betrag"""

    def get(self, request, nr):
        try:
            customer = get_object_or_404(Customer, nr=nr)
            saldo = customer.saldo
            name = customer.name

            actions = Action.objects.filter(nr=nr)

            table = []
            if actions:
                table = actions.values_list('id', 'nr', 'datum', 'actiontype', 'betrag')

            data = {"nr": nr, "name" : name,"saldo": saldo}
            
            return render(request, 'balance.html', {'main': data, 'actions': table})
        except Http404:
            # Handle the case when no Transaktionen object is found
            return render(request, '404.html')

