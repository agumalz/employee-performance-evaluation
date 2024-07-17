from django.urls import path
from .views import data_input, data_calculate, data_main, data_delete, data_edit

urlpatterns = [
    path('data_main/', data_main, name='data_main'),
    path('data_input/', data_input, name='data_input'),
    path('data_calculate/', data_calculate, name='data_calculate'),
    path('data_delete/<int:id>/', data_delete, name='data_delete')
]