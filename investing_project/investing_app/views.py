from django.shortcuts import render, redirect, HttpResponse
from .models import Investment
from .forms import InvestmentForm
from django.contrib.auth.decorators import login_required


def investment(request):
    data = {
        'data': Investment.objects.all()
    }
    return render(request, 'investments/investments.html', context=data)


def detail(request, id_investment):
    data = {
        'data': Investment.objects.get(pk=id_investment)
    }
    return render(request, 'investments/detail.html', data)


@login_required
def create(request):
    if request.method == 'POST':
        investment_form = InvestmentForm(request.POST)
        if investment_form.is_valid():
            investment_form.save()
        return redirect('investments')
    else:
        investment_form = InvestmentForm()
        form_data = {
            'form_data': investment_form
        }
        return render(request, 'investments/new_investment.html', context=form_data)


@login_required
def edit(request, id_investment):
    investment = Investment.objects.get(pk=id_investment)

    if request.method == 'GET':
        form = InvestmentForm(instance=investment)
        return render(request, 'investments/new_investment.html', {'form_data': form})
    else:
        form = InvestmentForm(request.POST, instance=investment)
        if form.is_valid():
            form.save()
        return redirect('investments')


@login_required
def delete(request, id_investment):
    investment = Investment.objects.get(pk=id_investment)
    if request.method == 'POST':
        investment.delete()
        return redirect('investments')
    return render(request, 'investments/confirm_delete.html', {'item': investment})
