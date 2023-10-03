from django.contrib import admin
from django.urls import path, include
from jcf import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='jcf'),
    path('contacts/', views.contacts, name='contacts'),
    path('special/', views.special, name='special'),
    path('about/', views.about, name='about')

]