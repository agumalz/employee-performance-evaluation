from django.shortcuts import render
from KaryawanKriteria.models import KaryawanKriteria, Crew
from .fuzzy_logic import fuzzifikasi, calculate_alpha_predicate_and_z, rules

# View untuk menampilkan hasil fuzzifikasi untuk semua karyawan
def fuzzifikasi_view(request):
    karyawan_list = Crew.objects.all()
    fuzzifikasi_results = []

    for karyawan in karyawan_list:
        karyawan_kriteria = KaryawanKriteria.objects.filter(karyawan=karyawan)
        kriteria_dict = {}
        for item in karyawan_kriteria:
            kriteria_dict[item.kriteria.nama] = fuzzifikasi(item.nilai)
        fuzzifikasi_results.append({
            'karyawan': karyawan,
            'kriteria_dict': kriteria_dict,
        })

    context = {
        'fuzzifikasi_results': fuzzifikasi_results,
    }
    return render(request, 'fuzzifikasi.html', context)

# View untuk menampilkan hasil inferensi (alpha predikat dan z) untuk semua karyawan
def inferensi_view(request):
    karyawan_list = Crew.objects.all()
    inferensi_results = []

    for karyawan in karyawan_list:
        karyawan_kriteria = KaryawanKriteria.objects.filter(karyawan=karyawan)
        kriteria_dict = {}
        karyawan_inferensi = []

        for item in karyawan_kriteria:
            kriteria_dict[item.kriteria.nama] = fuzzifikasi(item.nilai)

        for rule in rules:
            alpha_predikat, z = calculate_alpha_predicate_and_z(kriteria_dict, rule)
            karyawan_inferensi.append({
                'rule': rule,
                'alpha_predikat': alpha_predikat,
                'z': z,
            })

        inferensi_results.append({
            'karyawan': karyawan,
            'karyawan_inferensi': karyawan_inferensi,
        })

    context = {
        'inferensi_results': inferensi_results,
    }
    return render(request, 'inferensi.html', context)

# View untuk menampilkan hasil defuzzifikasi (hasil akhir) untuk semua karyawan
def defuzzifikasi_view(request):
    karyawan_list = Crew.objects.all()
    defuzzifikasi_results = []

    for karyawan in karyawan_list:
        karyawan_kriteria = KaryawanKriteria.objects.filter(karyawan=karyawan)
        kriteria_dict = {}
        total_alpha_z = 0
        total_alpha = 0

        for item in karyawan_kriteria:
            kriteria_dict[item.kriteria.nama] = fuzzifikasi(item.nilai)

        for rule in rules:
            alpha_predikat, z = calculate_alpha_predicate_and_z(kriteria_dict, rule)
            total_alpha_z += alpha_predikat * z
            total_alpha += alpha_predikat

        if total_alpha != 0:
            hasil_akhir = total_alpha_z / total_alpha
        else:
            hasil_akhir = 0  # Atau nilai default lain jika total_alpha = 0

        # Tentukan kinerja berdasarkan nilai akhir hasil defuzzifikasi
        if hasil_akhir > 50:
            kinerja = "Baik"
        else:
            kinerja = "Buruk"

        defuzzifikasi_results.append({
            'karyawan': karyawan,
            'hasil_akhir': hasil_akhir,
            'kinerja': kinerja,
        })

    context = {
        'defuzzifikasi_results': defuzzifikasi_results,
    }
    return render(request, 'defuzzifikasi.html', context)

from kriteria.models import Kriteria  # Pastikan Anda mengimpor model Kriteria
from crew.models import Crew
from KaryawanKriteria.models import KaryawanKriteria

def karyawan_kriteria_overview(request):
    karyawan_list = Crew.objects.all()
    kriteria_list = Kriteria.objects.all()  # Dapatkan semua kriteria
    penilaian_data = []

    for karyawan in karyawan_list:
        nilai_kriteria = KaryawanKriteria.objects.filter(karyawan=karyawan)
        penilaian_data.append({
            'karyawan': karyawan,
            'nilai_kriteria': nilai_kriteria,
        })

    context = {
        'karyawan_list': karyawan_list,
        'kriteria_list': kriteria_list,
        'penilaian_data': penilaian_data,
    }
    return render(request, 'karyawan_kriteria_overview.html', context)
