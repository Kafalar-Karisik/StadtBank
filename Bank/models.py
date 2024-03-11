"""Bank/models.py"""
from django.db import models


class Customer(models.Model):
    """Customer Class"""
    nr = models.IntegerField(primary_key=True)
    name = models.TextField()
    balance = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        """Customer.Meta Class"""
        db_table = 'customers'


class Action(models.Model):
    """Action Class"""
    id = models.IntegerField(primary_key=True, auto_created=True)
    nr = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    type = models.TextField(choices=[('payin', 'Pay In'),
                                     ('payout', 'Pay Out'),
                                     ('transfer', 'Transfer')])
    amount = models.FloatField()
    related_nr = models.IntegerField(null=True)
    before = models.IntegerField(null=True)

    def __str__(self):
        return f"Action {self.id}"

    def getNames(self):
        """Action.getNames Function"""
        try:
            return Customer.objects.get(nr=self.nr).name, Customer.objects.get(nr=self.related_nr).name
        except:
            return Customer.objects.get(nr=self.nr).name, None

    class Meta:
        """Action.Meta Class"""
        db_table = 'actions'
