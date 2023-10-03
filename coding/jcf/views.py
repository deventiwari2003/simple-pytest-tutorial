from django.shortcuts import render, HttpResponse
from datetime import datetime
from jcf.models import Contacts
#from django.contrib.messages import constants as messages
from django.contrib import messages
#import requests
# Create your views here.

def index(request):
    if request.method == "POST":
        pass
        return

    context = {
        "variable": "God wants everyone to live in peace",
        "charlie": {
            "roger": "mighty",
            "peter": "fearless"
        }
    }
    return render(request,'index.html', context)

def contacts(request):
    context = {
        "variable": "God wants everyone to live in peace",
        "charlie": {
            "roger": "mighty",
            "peter": "fearless"
        }
    }
    #messages.success(request, f"Test message")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contacts = Contacts(name=name, email=email,
                            phone=phone,desc=desc,date_posted=datetime.today())
        contacts.save()
        messages.success(request, f"Contact for {name} saved")
        return render(request,'contacts.html')
    return render(request,'contacts.html', context)

def special(request):
    return render(request,'special.html')

def about(request):
    return render(request,'about.html')