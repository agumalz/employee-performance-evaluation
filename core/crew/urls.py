from django.urls import path
from . import views

urlpatterns = [
    path('', views.crew_main, name='crew_main')
]
