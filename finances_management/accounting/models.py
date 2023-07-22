from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import Sum, F, Prefetch


class Customer(models.Model):
    telegram_id = models.PositiveBigIntegerField(
        verbose_name='Telegram ID',
        unique=True,
        db_index=True,
    ),

    class Meta:
        verbose_name = 'User ID'


class Wallet(models.Model):
    user = models.ForeignKey(
        'accounting.Customer',
        verbose_name='User ID',
        related_name='wallets',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Wallet name',
        default='total',
        max_length=60,
    )
    balance = models.DecimalField(
        verbose_name='Current balance',
        default=0,
        max_digits=9,
        decimal_places=2,
    )

    class Meta:
        verbose_name = 'Wallet'


class Transaction(models.Model):
    transaction_types = [
        ('in', 'income'),
        ('ex', 'expanse')
    ]

    wallet = models.ForeignKey(
        'accounting.Wallet',
        verbose_name='wallet',
        related_name='transactions',
        on_delete=models.CASCADE,
    )
    value = models.DecimalField(
        verbose_name='Amount',
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    description = models.TextField(
        verbose_name='Description',
        max_length=1000,
        blank=True,

    )
    date = models.DateTimeField(
        verbose_name='Transaction date',
        auto_now_add=True,
    )
    type_of_transaction = models.CharField(max_length=60, choices=transaction_types)

    class Meta:
        verbose_name = 'Income'
