from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm


def homeView(request):
    count = User.objects.count()
    return render(request, 'home.html', {'count': count})


def signupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})
