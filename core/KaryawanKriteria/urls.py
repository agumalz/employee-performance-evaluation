from django.urls import path
from . import views

urlpatterns = [
    path('', views.karyawan_kriteria_list, name='karyawan_kriteria_list'),
    path('create/', views.karyawan_kriteria_create, name='karyawan_kriteria_create'),
    path('edit/<int:karyawan_id>/', views.karyawan_kriteria_edit, name='karyawan_kriteria_edit'),
    path('delete/<int:karyawan_id>/', views.karyawan_kriteria_delete, name='karyawan_kriteria_delete'),
]
