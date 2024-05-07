"""Django Modules"""
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import (Http404, HttpResponse,  # HttpResponse,
                         HttpResponseRedirect)
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from bin import TOTP  # ignore

from .forms import CreditF, CustomerF, PayF, TransferF, newCustomerF
from .models import Action, Credit, Customer


def index(request) -> HttpResponse:
    """Index Page"""

    return render(request, 'dashboard.html',
                  {'customers': Customer.objects.all(),
                   'actions': Action.objects.select_related('customer', 'related').all()})


class Actions(View):
    """Actions Page"""

    def get(self, request) -> HttpResponse:
        """Actions.get"""
        return render(request, 'actions.html', {'actions': Action.objects.all()})


class Customers(View):
    """Customers Page"""

    def get(self, request) -> HttpResponse:
        """Customers.get"""
        return render(request, 'customers.html', {'customers': Customer.objects.all()})


class CustomerDV(View):
    """Customer Detail View page"""

    def get(self, request, nr) -> HttpResponse:
        """CustomerDV.get"""
        try:
            customer = get_object_or_404(Customer, nr=nr)

            actions = Action.objects.filter(customer=nr)

            return render(request, 'customer.html', {'customer': customer, 'actions': actions})
        except Http404:
            return render(request, '404.html')


class ActionDV(View):
    """Action Detail View page"""

    def get(self, request, nr) -> HttpResponse:
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
            return render(request, '404.html')


class Pay(View):
    """Pay Page"""
    customers = Customer.objects.all()

    def get(self, request) -> HttpResponse:
        """Pay.get"""
        return render(request, 'pay.html', {'customers': self.customers})


class CreditManagment(View):
    """Credit Page"""
    actions = Action.objects.all()
    customers = Customer.objects.all()

    def get(self, request) -> HttpResponse:
        """Credit.get"""
        return render(request, 'credit.html', {'customers': self.customers, 'actions': self.actions})


def pay_in(request) -> HttpResponseRedirect:
    """payIn API (Not Used)"""

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


def pay_out(request) -> HttpResponseRedirect:
    """PayOut API (Not Used)"""

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


@login_required
def pay(request) -> HttpResponseRedirect:
    """Pay API"""
    if request.method == "POST":
        form = PayF(request.POST)
        if form.is_valid():
            payType = request.POST.get("type")
            if payType == "payin":
                datas = form.cleaned_data
                target = datas["customer"]
                before = target.balance
                target.balance += datas["amount"]
                target.save()

                Action(customer=datas["customer"], type="payin",
                       amount=datas["amount"], before=before).save()

            elif payType == "payout":
                datas = form.cleaned_data
                target = datas["customer"]
                before = target.balance
                target.balance -= datas["amount"]
                target.save()

                Action(customer=datas["customer"], type="payout",
                       amount=datas["amount"], before=before).save()

    return HttpResponseRedirect("/pay")


def transfer(request) -> HttpResponseRedirect:
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
                customer=datas["nr"],
                related=datas["related"],
                type="transfer",
                amount=datas["amount"]
            )
            action.save()

    return HttpResponseRedirect("/pay")


@login_required
def newCustomer(request) -> HttpResponseRedirect:
    """NewCustomer API"""
    if request.method == "POST":
        form = newCustomerF(request.POST)

        if form.is_valid():
            datas = form.cleaned_data
            customer = Customer(name=datas["name"])

            customer.save()
    return HttpResponseRedirect("/customers")


@login_required
def credit(request) -> HttpResponseRedirect:
    """Crediy API"""
    if request.method == "POST":
        form = CreditF(request.POST)
        if form.is_valid():
            datas = form.cleaned_data
            target = datas["customer"]
            amount = datas["amount"]

            Credit(customer=target, amount=amount).save()
            target.credits = target.credits + amount

            target.save()
    return HttpResponseRedirect("/creditManagment")


class Login(View):
    """Login Page"""

    def get(self, request):
        """Login.get"""
        return render(request, 'login.html',
                      {'next': request.GET["next"]} if "next" in request.GET else None)

    def post(self, request):
        """Login.post"""
        passw = request.POST["passw"]
        user = authenticate(request, username="worker", password=passw)
        if user is not None:
            login(request, user)

        if 'next' in request.GET and url_has_allowed_host_and_scheme(
                request.GET['next'], allowed_hosts=None):
            return HttpResponseRedirect(request.GET["next"])

        return redirect('/')


@csrf_exempt
def newWorkerPass(request) -> HttpResponse:
    """New Worker Password API"""
    if request.method == "POST":
        passw = TOTP.newWorkerPassword(request.POST['password'])
        return HttpResponse(passw)

    return HttpResponseRedirect("/")
