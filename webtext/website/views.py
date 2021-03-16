
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_safe
from rest_framework import status

from website.forms import LoginForm


@require_http_methods(['GET', 'POST'])
def anon_login(request):

    if request.user.is_authenticated:
        return redirect("app-index")

    if request.method == "GET":
        return render(request, "login.html", {})

    elif request.method == "POST":
        form = LoginForm(request.POST)
        if not form.is_valid():
            data = {
                "login_error":"Invalid username/password",
            }
            return render(request, 'login.html', data)

        user = authenticate(
            request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'])
        if user is not None:
            login(request, user)
            return redirect('app-index')
        else:
            data = {
                "login_error":"Invalid username/password",
                "attempted_username":form.cleaned_data['username'],
            }
            return render(request, 'login.html', data)

    else:
        raise NotImplementedError()


@require_safe
def app_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("anon-login")


@require_safe
@login_required
def app_index(request):
    return render(request, 'index.html', {})
