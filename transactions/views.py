from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Transaction


# Create your views here.
@login_required
def add_transaction(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        transaction_type = request.POST.get('transaction_type')

        Transaction.objects.create(
            user=request.user,
            title=title,
            amount=amount,
            category=category,
            transaction_type=transaction_type
        )

        return redirect('home')
    
    return render(request, 'add_transactions.html')


@login_required
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(
        Transaction,
        id=transaction_id,
        user=request.user
    )

    if request.method == 'POST':
        transaction.delete()
        return redirect('home')
    
    return redirect('home')


@login_required
def edit_transaction(request, transaction_id):

    transaction = get_object_or_404(
        Transaction,
        id=transaction_id,
        user=request.user
    )

    if request.method == 'POST':


        transaction.title = request.POST.get('title')
        transaction.amount = request.POST.get('amount')
        transaction.category = request.POST.get('category')
        transaction.transaction_type = request.POST.get('transaction_type')

        transaction.save()

        return redirect('home')
    
    context = {
        'transaction' : transaction
    }
    
    return render(
        request,
        'edit_transaction.html',
        context
    )
    
