from django import forms
from .models import Expense, Income


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense

        fields = ('title', 'expense')
        exclude = ('user',)


class IncomeForm(forms.ModelForm):

    class Meta:
        model = Income

        fields = ('title', 'income')
        exclude = ('user',)
