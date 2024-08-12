from django.urls import path
from . import views

urlpatterns = [
    path('overview/', views.karyawan_kriteria_overview, name='karyawan_kriteria_overview'),
    path('fuzzifikasi_view/', views.fuzzifikasi_view, name='fuzzifikasi_view'),
    path('inferensi_view/', views.inferensi_view, name='inferensi_view'),
    path('defuzzifikasi_view/', views.defuzzifikasi_view, name='defuzzifikasi_view'),
]

