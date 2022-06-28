from django.contrib import admin
from django.urls import path,include
from .import views 
urlpatterns = [
    path('',views.add,name="home"),
    path('insert',views.insert),
    path('delete/<str:pk>',views.delete,name="delete"),
    path('update',views.update,name="update")
]