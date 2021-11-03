from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User


def user(request):
    form = UserForm()
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create(first_name=cd['first_name'],
                                last_name=cd['last_name'],
                                age=cd['age'],
                                email=cd['email'],
                                phone_number=cd['phone_number']
                                )
            return redirect('user')
    return render(request, 'user_form.html', {'form': form})


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})
