from django.contrib import admin
from .models import Balance, Expense, Income

admin.site.register(Balance)
admin.site.register(Expense)
admin.site.register(Income)
