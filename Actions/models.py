"""Django Module(s)"""
from django.db import models


class Customer(models.Model):
    """Customer Class"""
    nr = models.IntegerField(primary_key=True)
    name = models.TextField()
    balance = models.ImageField()

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        """Customer.Meta Class"""
        db_table = 'customers'


class Action(models.Model):
    """Action Class"""
    id = models.AutoField(primary_key=True)
    nr = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    type = models.TextField(choices=[('payin', 'Pay In'),
                                     ('payout', 'Pay Out'),
                                     ('transfer', 'Transfer')])
    amount = models.FloatField()
    related_nr = models.IntegerField(null=True)

    def __str__(self):
        return f"Action {self.id}"

    class Meta:
        """Action.Meta Class"""
        db_table = 'actions'
