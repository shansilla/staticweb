from . import views
from django.urls import path

urlpatterns = [

    path('', views.demo, name='demo'),
    # path('result/', views.home, name='home')

]