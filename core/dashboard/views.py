from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.http import JsonResponse
from crew.models import Crew  # Model untuk data karyawan
from KaryawanKriteria.models import KaryawanKriteria
from crew.models import Crew
from kriteria.models import Kriteria

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


COLOR_PALETTE = [
    "rgba(255, 99, 132, 0.5)",  # Merah
    "rgba(54, 162, 235, 0.5)",  # Biru
    "rgba(255, 206, 86, 0.5)",  # Kuning
    "rgba(75, 192, 192, 0.5)",  # Hijau
    "rgba(153, 102, 255, 0.5)",  # Ungu
    "rgba(255, 159, 64, 0.5)",  # Orange
]

BORDER_PALETTE = [
    "rgba(255, 99, 132, 1)", 
    "rgba(54, 162, 235, 1)", 
    "rgba(255, 206, 86, 1)", 
    "rgba(75, 192, 192, 1)", 
    "rgba(153, 102, 255, 1)", 
    "rgba(255, 159, 64, 1)",
]

def dashboard_chart_data(request):
    """API untuk mengambil data penilaian karyawan dalam format JSON."""

    karyawan_list = Crew.objects.all()
    kriteria_list = Kriteria.objects.all()

    chart_data = {
        "labels": [karyawan.nama for karyawan in karyawan_list],
        "datasets": []
    }

    for index, kriteria in enumerate(kriteria_list):
        nilai_karyawan = []

        for karyawan in karyawan_list:
            try:
                nilai = KaryawanKriteria.objects.get(karyawan=karyawan, kriteria=kriteria).nilai
            except KaryawanKriteria.DoesNotExist:
                nilai = 0

            nilai_karyawan.append(nilai)

        chart_data["datasets"].append({
            "label": kriteria.nama,
            "data": nilai_karyawan,
            "backgroundColor": COLOR_PALETTE[index % len(COLOR_PALETTE)],  # Pilih warna sesuai index
            "borderColor": BORDER_PALETTE[index % len(BORDER_PALETTE)],
            "borderWidth": 1
        })

    return JsonResponse(chart_data)
