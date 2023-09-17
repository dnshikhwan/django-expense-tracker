from django.urls import path
from . import views

urlpatterns = [
    path('', views.acc_balance, name='acc-balance'),
    path('add-expense', views.add_expense, name='add-expense'),
    path('add-income', views.add_income, name='add-income'),
]
