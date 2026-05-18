from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from transactions.models import Transaction
from django.db.models import Sum

@login_required
def home(request):

    transactions= Transaction.objects.filter(
        user=request.user
    )

    search_query = request.GET.get('search')

    category = request.GET.get('category')

    transaction_type = request.GET.get('type')

    if search_query:
        transactions = transactions.filter(
            title__icontains=search_query
        )

    if category:
        transactions= transactions.filter(
            category=category
        )  

    if transaction_type:
       transactions =  transactions.filter(
           transactions_type=transaction_type
       )     

    transactions = transactions.order_by('-created_at')

    total_income = Transaction.objects.filter(
        user=request.user,
        transaction_type='Income'
    ).aggregate(Sum('amount'))['amount__sum'] or 0   

    total_expense = Transaction.objects.filter(
        user=request.user,
        transaction_type='Expense'
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    balance = total_income - total_expense
    

    context = {
        'transactions' : transactions,
        'total_income' : total_income,
        'total_expense': total_expense,
        'balance' : balance,
    }


    return render(request, 'home.html', context)

# Create your views here.
