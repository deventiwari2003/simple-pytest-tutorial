from django.contrib import admin
from django.urls import path
from carx import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('show_all/', views.car_show_all, name="car_show_all"),
    path('add_car/', views.add_car, name="add_car"),
    path('upd_car/<str:id>', views.upd_car, name="upd_car"),
    path('del_car/', views.del_car, name="del_car"),
]