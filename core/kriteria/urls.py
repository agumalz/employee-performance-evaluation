from django.urls import path
from . import views

urlpatterns = [
    path('', views.kriteria_list, name='kriteria_list'), 
    path('kriteria_create/', views.kriteria_create, name='kriteria_create'),  
    path('kriteria_edit/<int:id>/', views.kriteria_edit, name='kriteria_edit'),  
    path('kriteria_delete/<int:id>/', views.kriteria_delete, name='kriteria_delete'),  
]
