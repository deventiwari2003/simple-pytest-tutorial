from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from myapp.forms import SignupForm, LoginForm

# Create your views here.
def myapp_signup(request):
    print("myapp_signup")
    context = {
        'page_name': "myapp_signup",
    }
    if request.method == "POST":
        form = SignupForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect("myapp_login")
        else:
            print("check inputs")
    else:
        form = SignupForm()
        context['form'] = form
    return render(request, "myapp_signup.html", context=context)


def myapp_login(request):
    context = {
        'page_name': "myapp_login",
    }
    if request.method == "POST":
        form = LoginForm(request.POST)
        context['form'] = form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = authenticate(request,username=username,password=password,email=email)
            if user:
                login(request, user)
                return redirect("car_show_all")
        else:
            print("check user inputs")
    else:
        form = LoginForm()
        context['form'] = form
    return render(request, "myapp_login.html", context=context)

def myapp_logout(request):
    logout(request)
    return redirect("myapp_login")
