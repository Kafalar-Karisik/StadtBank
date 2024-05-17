# Generated by Django 5.0.3 on 2024-05-17 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('nr', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField()),
                ('balance', models.IntegerField(default=0)),
                ('credits', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True)),
                ('value', models.JSONField()),
            ],
            options={
                'db_table': 'settings',
            },
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('payBack', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bank.customer')),
            ],
            options={
                'db_table': 'credits',
            },
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('type', models.TextField(choices=[('payin', 'Pay In'), ('payin-salary', 'Pay In (Salary)'), ('payout', 'Pay Out'), ('transfer', 'Transfer'), ('take-credit', 'Take Credit'), ('pay-credit', 'Pay Credit')])),
                ('amount', models.IntegerField(null=True)),
                ('before', models.IntegerField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_customer', to='Bank.customer')),
                ('related', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='action_related', to='Bank.customer')),
            ],
            options={
                'db_table': 'actions',
            },
        ),
    ]
