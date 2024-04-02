"""Bank/models.py"""

from django.db import models


class Customer(models.Model):
    """Customer Class"""
    nr = models.IntegerField(
        primary_key=True, unique=True, auto_created=False)
    name = models.TextField()
    balance = models.IntegerField(default=0)
    credits = models.IntegerField(default=0, null=True)

    def __str__(self) -> str:
        return f"{self.name} | {self.nr}"

    class Meta:
        """Customer.Meta Class"""
        db_table = 'customers'


class Action(models.Model):
    """Action Class"""
    id = models.IntegerField(
        primary_key=True, auto_created=True)
    customer = models.ForeignKey(
        Customer, related_name="action_customer", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    type = models.TextField(choices=[('payin', 'Pay In'),
                                     ('payout', 'Pay Out'),
                                     ('transfer', 'Transfer')])
    amount = models.IntegerField(null=True)
    related = models.ForeignKey(
        Customer, related_name="action_related", on_delete=models.CASCADE, null=True)
    before = models.IntegerField(null=True)

    def __str__(self):
        return f"Action {self.id}"

    class Meta:
        """Action.Meta Class"""
        db_table = 'actions'


class Credit(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Action.Meta Class"""
        db_table = 'credits'
