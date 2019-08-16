from django.urls import path
from . import views

urlpatterns=[

path('',views.spacef,name='ApiAPP'),
path('add_data/',views.add_data,name='Adding'),



]