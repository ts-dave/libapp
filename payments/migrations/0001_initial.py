# Generated by Django 5.0 on 2023-12-22 11:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0002_alter_book_language_alter_book_link_alter_book_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fine_date', models.DateTimeField(auto_now=True)),
                ('fine_amount', models.DecimalField(decimal_places=2, max_digits=4)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fines', to='library.loan')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fines', to='library.member')),
            ],
        ),
        migrations.CreateModel(
            name='FinePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now=True)),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='library.member')),
            ],
        ),
    ]