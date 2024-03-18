from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout


def new_user(request):
    # validate, inform, save
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # inform
            user = form.cleaned_data.get('username')
            messages.success(request, f'The user {
                             user} was created successfully!')
            return redirect('login')
            # save
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
