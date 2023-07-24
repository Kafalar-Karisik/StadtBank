from django.db import models


class Customer(models.Model):
    nr = models.IntegerField(primary_key=True)
    name = models.TextField()
    saldo = models.FloatField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'customers'


class Action(models.Model):
    id = models.AutoField(primary_key=True)
    nr = models.IntegerField()
    datum = models.DateTimeField(auto_now_add=True)
    actiontype = models.TextField()
    betrag = models.FloatField()
    kunde = models.ForeignKey('Action', on_delete=models.CASCADE)

    def __str__(self):
        return f"Action {self.id}"

    class Meta:
        db_table = 'actions'