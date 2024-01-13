# Generated by Django 5.0 on 2023-12-24 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fine',
            old_name='fine_amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='fine',
            old_name='fine_date',
            new_name='date',
        ),
        migrations.AddField(
            model_name='finepayment',
            name='fine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payments', to='payments.fine'),
        ),
    ]