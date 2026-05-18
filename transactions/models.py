from django.db import models
from django.contrib.auth.models import User


CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Shopping','Shopping'),
        ('Bills', 'Bills'),
        ('Salary', 'Salary'),
    ]


TRANSACTION_TYPES = [
        ('Income', 'Income'),
        ('Expense','Expense'),
    ]

# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPES
    )


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title