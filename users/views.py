from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from . import forms


# Create your views here.
def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, "users/login_user.html", {"form": form})


def signup_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        form2 = forms.CreateExtendedUser(request.POST)
        if form.is_valid() and form2.is_valid():
            user = form.save(commit=False)
            extendedform = form2.save(commit=False)
            user.save()
            extendedform.user = user
            extendedform.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        form2 = forms.CreateExtendedUser()
    return render(request, "users/signup_user.html", {"form": form, "form2": form2})


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


def login_org(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, "users/login_org.html", {"form": form})


def signup_org(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        form2 = forms.CreateOrg(request.POST)
        if form.is_valid() and form2.is_valid():
            user = form.save(commit=False)
            orgform = form2.save(commit=False)
            user.save()
            orgform.user = user
            orgform.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        form2 = forms.CreateOrg()
    return render(request, "users/signup_org.html", {"form": form, "form2": form2})
