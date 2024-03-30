"""Django Module(s)"""
from django.http import Http404, HttpResponseRedirect  # HttpResponse,
from django.shortcuts import get_object_or_404, render
from django.views import View

from Bank.models import Action, Customer

from .forms import CustomerF, PayForm, TransferF

# Create your views here.
# pylint: disable=no-member


def index(request):
    """Index Page"""
    customers = Customer.objects.all()
    actions = Action.objects.all()

    names = {"customers": [], "actions": [[], []]}

    return render(request, 'dashboard.html', {'customers': customers,
                                              'actions': actions,
                                              'names': names})


class Actions(View):
    """Actions Page"""

    def get(self, request):
        """Actions.get"""
        return render(request, 'actions.html', {'actions': Action.objects.all()})


class Customers(View):
    """Customers Page"""

    def get(self, request):
        """Customers.get"""
        return render(request, 'customers.html', {'customers': Customer.objects.all()})


class CustomerDV(View):
    """Customer Detail View page"""
    # ID, Numer, Date, Type, Balance

    def get(self, request, nr):
        """CustomerDV.get"""
        try:
            customer = get_object_or_404(Customer, nr=nr)

            actions = Action.objects.filter(customer=nr)

            return render(request, 'customer.html', {'customer': customer, 'actions': actions})
        except Http404:
            # Handle the case when no Transaktionen object is found
            return render(request, '404.html')


class ActionDV(View):
    """Action Detail View page"""
    # ID, Numer, Date, ActionType, amount, related

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


class Pay(View):
    """Pay Page"""
    customers = Customer.objects.all()

    def get(self, request):
        """Pay.get"""
        return render(request, 'pay.html', {'customers': self.customers})


class Credit(View):
    """Credit Page"""

    def get(self, request):
        """Credit.get"""
        return render(request, 'credit.html')


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


def pay(request):
    if request.method == "POST":
        form = PayForm(request.POST)
        if form.is_valid():
            type = request.POST.get("type")
            if type == "payin":
                datas = form.cleaned_data
                target = datas["customer"]
                before = target.balance
                target.balance += datas["amount"]
                target.save()

                action = Action(
                    customer=datas["customer"], type="payin", amount=datas["amount"], before=before)
                action.save()

            elif type == "payout":
                datas = form.cleaned_data
                target = Customer.objects.get(nr=datas["customer"])
                before = target.balance
                target.balance -= datas["amount"]
                target.save()

                action = Action(
                    customer=datas["customer"], type="payout", amount=datas["amount"], before=before)
                action.save()
        else:
            print("NONOno")

    return HttpResponseRedirect("/#")


def transfer(request):
    """Transfer API"""
    if request.method == "POST":
        form = TransferF(request.POST)

        if form.is_valid():
            datas = form.cleaned_data
            customer = datas["nr"]
            customer1 = datas["related"]
            amount = datas["amount"]
            customer.balance -= amount
            customer1.balance += amount
            customer.save()
            customer1.save()

            action = Action(
                nr=datas["nr"], related=datas["related"], type="transfer", amount=datas["amount"]
            )
            action.save()
        else:
            print("Not Valid")
    return HttpResponseRedirect("./#")


class Settings(View):
    """Settings Page"""

    def get(self, request):
        """Settings.get"""
        return render(request, 'settings.html')
