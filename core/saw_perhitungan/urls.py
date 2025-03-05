from django.urls import path
from .views import saw_konversi_view, saw_normalisasi_view, saw_ranking_view, karyawan_kriteria_overview_baik, hasil_perhitungan_view

urlpatterns = [
    path('karyawan_kriteria_overview_baik/', karyawan_kriteria_overview_baik, name='karyawan_kriteria_overview_baik'),
    path('saw_konversi/', saw_konversi_view, name='saw_konversi_view'),
    path('saw_normalisasi/', saw_normalisasi_view, name='saw_normalisasi_view'),
    path('saw_ranking/', saw_ranking_view, name='saw_ranking_view'),
    path('hasil_perhitungan_view/', hasil_perhitungan_view, name='hasil_perhitungan_view'),
]
