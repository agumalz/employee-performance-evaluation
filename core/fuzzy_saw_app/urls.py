from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_main, name='data_main'),
    path('edit/<int:id>/', views.data_edit, name='data_edit'),
    path('input/', views.data_input, name='data_input'),
    path('delete/<int:id>/', views.data_delete, name='data_delete'),
    path('calculate/', views.data_calculate, name='data_calculate'),
    path('visualisasi_data/', views.visualisasi_data, name='visualisasi_data'),
]
