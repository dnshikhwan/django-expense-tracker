from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Balance(models.Model):
    total = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' - ' + str(self.total)


class Expense(models.Model):
    title = models.CharField(max_length=20)
    expense = models.DecimalField(default=0, decimal_places=2, max_digits=8)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + str(self.expense)


class Income(models.Model):
    title = models.CharField(max_length=20)
    income = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + str(self.income)
