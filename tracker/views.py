from django.shortcuts import render, redirect
from .models import Balance, Expense, Income
from .forms import ExpenseForm, IncomeForm
from django.contrib.auth.models import User
from django.db.models import Sum, Count


def acc_balance(request):
    balances = Balance.objects.filter(user=request.user).values('total')
    expenses = Expense.objects.filter(user=request.user)
    total_expense = Expense.objects.aggregate(Sum('expense'))
    incomes = Income.objects.filter(user=request.user)
    total_income = Income.objects.aggregate(Sum('income'))

    # items() only for dict
    for key, value in total_expense.items():
        sum_expense = value

    # for query set
    for item in balances:
        balance = item['total']

    for key, value in total_income.items():
        sum_income = value

    account_balance = balance - sum_expense + sum_income

    context = {
        'account_balance': account_balance,
        'expenses': expenses,
        'total_expense': total_expense,
        'incomes': incomes,
        'total_income': total_income,
        'status_labels': ['Income', 'Expense'],
        'status_counts': [float(sum_income), float(sum_expense)]
    }

    return render(request, 'tracker/balance.html', context=context)


def add_expense(request):
    expense_form = ExpenseForm()

    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            form = expense_form.save(commit=False)
            # assign the user pk
            form.user = request.user
            form.save()
            return redirect('acc-balance')

    context = {
        'expense_form': expense_form
    }

    return render(request, 'tracker/add-expense.html', context=context)


def add_income(request):
    income_form = IncomeForm()

    if request.method == 'POST':
        income_form = IncomeForm(request.POST)
        if income_form.is_valid():
            form = income_form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('acc-balance')

    context = {
        'income_form': income_form
    }

    return render(request, 'tracker/add-income.html', context=context)
