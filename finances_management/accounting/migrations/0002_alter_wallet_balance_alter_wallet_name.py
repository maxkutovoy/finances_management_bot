# Generated by Django 4.2.3 on 2023-07-22 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Current balance'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='name',
            field=models.CharField(default='total', max_length=60, verbose_name='Wallet name'),
        ),
    ]
