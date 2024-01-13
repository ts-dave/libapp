# Generated by Django 5.0 on 2023-12-22 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='link',
            field=models.URLField(blank=True, default='www.com'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.CharField(default='1992', max_length=4),
            preserve_default=False,
        ),
    ]