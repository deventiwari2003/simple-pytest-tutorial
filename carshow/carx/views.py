import uuid

from django.shortcuts import render, HttpResponse
from utils.valdx import Valdx
from datetime import datetime
from carx.models import Car
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/myapp_login/")
def index(request):
    context = {
        "page_name" : "Index Main Page"
    }
    return render(request,'index.html',context=context)

@login_required(login_url="/myapp_login/")
def car_show_all(request):
    context = {
        "page_name": "Car Show All Page",
        'qset': Car.objects.all(),

    }
    print(context['qset'])
    return render(request, 'car_show_all.html', context=context)

@login_required(login_url="/myapp_login/")
def upd_car(request,id):
    context = {
        "page_name": "Update Car"
    }
    Car.objects.filter(id=uuid)
    obj = Car.objects.get(uuid(id))

@login_required(login_url="/myapp_login/")
def del_car(request):
    pass

@login_required(login_url="/myapp_login/")
def add_car(request):
    context = {
        "page_name": "Add Car"
    }
    flag = True
    vx = Valdx()
    msgx = ""
    if request.method == "POST":
        name = request.POST.get('name')
        mileage = request.POST.get('mileage')
        avg_speed = request.POST.get('avg_speed')
        outx = vx.validate_decimal(mileage)
        mileage = outx[1]
        if (outx[0] == -1):
            msgx += "Invalid mileage; "
            flag = False

        outx = vx.validate_integer(avg_speed)
        avg_speed = outx[1]
        if (outx[0] == -1):
            msgx += "Invalid avg_speed; "
            flag = False
        date_posted = datetime.today()
        if flag:
            car = Car(id=uuid.uuid4(),name=name,mileage=mileage,avg_speed=avg_speed,date_posted=date_posted)
            car.save()
            messages.success(request,f"Car for {name} saved")
        else:
            messages.warning(request, f"Msg: {msgx}")
        return render(request, 'add_car.html', context=context)

    return render(request, 'add_car.html', context=context)
