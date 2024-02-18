"""Django Module(s)"""
from django.http import Http404, HttpResponseRedirect  # HttpResponse,
from django.shortcuts import get_object_or_404, render
from django.views import View

from Bank.models import Action, Customer

from .forms import CustomerF

# Create your views here.
# pylint: disable=no-member


def index(request):
    """Index Page"""
    customers = Customer.objects.all()
    actions = Action.objects.all()

    names = {"customers": [], "actions": [[], []]}

    for i in actions:
        try:
            names["actions"][1].append(
                customers.get(nr=i.related_nr).name)
        except:
            names["actions"][1].append("")
            pass

    return render(request, 'dashboard.html', {'customers': customers, 'actions': actions, 'names': names})


class Actions(View):
    """Actions Page"""

    def get(self, request):
        """Actions.get"""
        transaktionen = Action.objects.all()
        return render(request, 'actions.html', {'actions': transaktionen})


class Customers(View):
    """Customers Page"""

    def get(self, request):
        """Customers.get"""
        kunden = Customer.objects.all()
        return render(request, 'customers.html', {'customers': kunden})


class CustomerDV(View):
    """Customer Detail View page"""
    # ID, Numer, Date, Type, Balance

    def get(self, request, nr):
        """CustomerDV.get"""
        try:
            customer = get_object_or_404(Customer, nr=nr)
            saldo = customer.balance
            name = customer.name

            actions = Action.objects.filter(nr=nr)

            table = []
            if actions:
                table = actions.values_list(
                    'id', 'nr', 'date', 'type', 'amount')

            data = {"nr": nr, "name": name, "saldo": saldo}

            return render(request, 'customer.html', {'main': data, 'actions': table})
        except Http404:
            # Handle the case when no Transaktionen object is found
            return render(request, '404.html')


class ActionDV(View):
    """Action Detail View page"""
    # ID, Numer, Date, ActionType, amount, related_nr

    def get(self, request, nr):
        """CustomerDV.get"""
        try:
            customer = get_object_or_404(Customer, nr=nr)
            saldo = customer.balance
            name = customer.name

            actions = Action.objects.filter(nr=nr)

            table = []
            if actions:
                table = actions.values_list(
                    'id', 'nr', 'date', 'type')

            data = {"nr": nr, "name": name, "saldo": saldo}

            return render(request, 'customer.html', {'main': data, 'actions': table})
        except Http404:
            # Handle the case when no Transaktionen object is found
            return render(request, '404.html')


def pay_in(request):
    """payIn API"""

    if request.method == "POST":
        form = CustomerF(request.POST)

        if form.is_valid():
            datas = form.cleaned_data
            target = Customer.objects.get(nr=datas["nr"])
            target.balance += datas["amount"]
            target.save()

            action = Action(
                nr=datas["nr"], actiontype="payin", amount=datas["amount"])
            action.save()

        else:
            print("NotValid")

    return HttpResponseRedirect("/.")


def pay_out(request):
    """PayOut API"""

    if request.method == "POST":
        form = CustomerF(request.POST)

        if form.is_valid():
            datas = form.cleaned_data
            target = Customer.objects.get(nr=datas["nr"])
            target.balance -= datas["amount"]
            target.save()

            action = Action(
                nr=datas["nr"], actiontype="payout", amount=datas["amount"])
            action.save()

        else:
            print("NotValid")

    return HttpResponseRedirect("/.")


class Settings(View):
    """Settings Page"""

    def get(self, request):
        """Settings.get"""
        return render(request, 'settings.html')
