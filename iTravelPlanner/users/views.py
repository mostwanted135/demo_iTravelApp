from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def createUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('users-login')
    else:
        form = UserCreationForm()

    return render(request, "users/register.html", {"form": form})



def home(request):
    return render(request, "users/index.html")
