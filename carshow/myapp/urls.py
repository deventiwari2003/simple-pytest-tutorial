from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('myapp_login/', views.myapp_login,name="myapp_login"),
    path('myapp_signup/', views.myapp_signup,name="myapp_signup"),
    path('myapp_logout/', views.myapp_logout, name="myapp_logout"),
]