from django.shortcuts import render
from crew.models import Crew
from KaryawanKriteria.models import KaryawanKriteria
from perhitungan_fuzzy.models import PerhitunganFuzzy
from kriteria.models import Kriteria
from .models import HasilPerhitungan

def konversi_nilai(nilai):
    if nilai is None:
        return 0
    elif nilai <= 29:
        return 0
    elif nilai <= 49:
        return 0.25
    elif nilai <= 69:
        return 0.5
    elif nilai <= 89:
        return 0.75
    elif nilai <= 100:
        return 1
    else:
        return 0  # Nilai diluar rentang yang diharapkan

def normalisasi_nilai(kriteria, nilai_konversi, karyawan_list):
    if kriteria.jenis == 'benefit':
        max_value = max(konversi_nilai(KaryawanKriteria.objects.get(karyawan=karyawan, kriteria=kriteria).nilai) for karyawan in karyawan_list)
        return nilai_konversi / max_value if max_value else 0
    elif kriteria.jenis == 'cost':
        min_value = min(konversi_nilai(KaryawanKriteria.objects.get(karyawan=karyawan, kriteria=kriteria).nilai) for karyawan in karyawan_list)
        return min_value / nilai_konversi if nilai_konversi else 0
    return 0

def karyawan_kriteria_overview_baik(request):
    karyawan_list = Crew.objects.filter(fuzzy_perhitungan__kinerja="Baik").prefetch_related('fuzzy_perhitungan')
    kriteria_list = Kriteria.objects.all()
    overview_data = []

    for karyawan in karyawan_list:
        karyawan_data = {'karyawan': karyawan, 'nilai_kriteria': []}
        for kriteria in kriteria_list:
            try:
                nilai_kriteria = KaryawanKriteria.objects.get(karyawan=karyawan, kriteria=kriteria).nilai
            except KaryawanKriteria.DoesNotExist:
                nilai_kriteria = None
            karyawan_data['nilai_kriteria'].append({
                'kriteria': kriteria.nama,
                'nilai': nilai_kriteria,
            })
        overview_data.append(karyawan_data)

    context = {
        'kriteria_list': kriteria_list,
        'overview_data': overview_data,
    }
    return render(request, 'karyawan_kriteria_overview_baik.html', context)

def saw_konversi_view(request):
    kriteria_list = Kriteria.objects.all()
    karyawan_list = Crew.objects.filter(fuzzy_perhitungan__kinerja="Baik").prefetch_related('fuzzy_perhitungan')
    konversi_data = []

    for karyawan in karyawan_list:
        # Tambahkan nama karyawan ke dalam dictionary karyawan_data
        karyawan_data = {
            'karyawan_id': karyawan.id,
            'karyawan_nama': karyawan.nama,  # Tambahkan nama karyawan
            'kriteria_nilai': []
        }
        for kriteria in kriteria_list:
            try:
                nilai_kriteria = KaryawanKriteria.objects.get(karyawan=karyawan, kriteria=kriteria).nilai
            except KaryawanKriteria.DoesNotExist:
                nilai_kriteria = None
            nilai_konversi = konversi_nilai(nilai_kriteria)
            karyawan_data['kriteria_nilai'].append({
                'kriteria': kriteria.nama,
                'nilai_asli': nilai_kriteria,
                'nilai_konversi': nilai_konversi,
            })
        konversi_data.append(karyawan_data)

    context = {
        'konversi_data': konversi_data,
    }
    return render(request, 'saw_konversi.html', context)


def saw_normalisasi_view(request):
    kriteria_list = Kriteria.objects.all()
    karyawan_list = Crew.objects.filter(fuzzy_perhitungan__kinerja="Baik").prefetch_related('fuzzy_perhitungan')
    normalisasi_data = []

    for karyawan in karyawan_list:
        # Simpan ID dan nama karyawan di karyawan_data
        karyawan_data = {
            'karyawan_id': karyawan.id, 
            'karyawan_nama': karyawan.nama,  # Tambahkan nama karyawan
            'normalisasi_nilai': []
        }
        for kriteria in kriteria_list:
            try:
                nilai_kriteria = KaryawanKriteria.objects.get(karyawan=karyawan, kriteria=kriteria).nilai
            except KaryawanKriteria.DoesNotExist:
                nilai_kriteria = None
            nilai_konversi = konversi_nilai(nilai_kriteria)
            nilai_normalisasi = normalisasi_nilai(kriteria, nilai_konversi, karyawan_list)
            karyawan_data['normalisasi_nilai'].append({
                'kriteria': kriteria.nama,
                'nilai_normalisasi': nilai_normalisasi,
            })

        normalisasi_data.append(karyawan_data)

    # Simpan data normalisasi ke session (termasuk ID dan nama karyawan)
    request.session['normalisasi_data'] = normalisasi_data

    context = {
        'normalisasi_data': normalisasi_data,
        'kriteria_list': kriteria_list,
    }

    return render(request, 'saw_normalisasi.html', context)

def saw_ranking_view(request):
    kriteria_list = Kriteria.objects.all()
    karyawan_list = Crew.objects.filter(fuzzy_perhitungan__kinerja="Baik").prefetch_related('fuzzy_perhitungan')

    # Ambil data normalisasi dari session
    normalisasi_data = request.session.get('normalisasi_data', [])

    hasil_ranking = []
    for karyawan_data in normalisasi_data:
        total_score = 0
        karyawan = Crew.objects.get(id=karyawan_data['karyawan_id'])
        for kriteria_data in karyawan_data['normalisasi_nilai']:
            kriteria = Kriteria.objects.get(nama=kriteria_data['kriteria'])
            nilai_normalisasi = kriteria_data['nilai_normalisasi']
            total_score += nilai_normalisasi * kriteria.get_bobot()
        hasil_ranking.append({'karyawan': karyawan, 'total_score': total_score})

    # Urutkan hasil berdasarkan skor tertinggi
    hasil_ranking.sort(key=lambda x: x['total_score'], reverse=True)

    context = {
        'hasil_ranking': hasil_ranking,
    }
    return render(request, 'saw_ranking.html', context)

def hasil_perhitungan_view(request):
    # Ambil semua karyawan yang memiliki hasil perhitungan fuzzy
    karyawan_list = Crew.objects.filter(fuzzy_perhitungan__isnull=False)
    normalisasi_data = request.session.get('normalisasi_data', [])

    hasil_perhitungan = []
    for karyawan in karyawan_list:
        try:
            # Dapatkan hasil perhitungan fuzzy
            perhitungan_fuzzy = PerhitunganFuzzy.objects.get(karyawan=karyawan)
        except PerhitunganFuzzy.DoesNotExist:
            perhitungan_fuzzy = None

        # Cek apakah sudah ada hasil yang disimpan
        hasil_terbaru = HasilPerhitungan.objects.filter(karyawan=karyawan).first()

        if hasil_terbaru:
            # Jika sudah ada, ambil hasil yang tersimpan
            total_score = hasil_terbaru.total_score
        else:
            # Jika belum ada, lakukan perhitungan
            total_score = 0
            for data in normalisasi_data:
                if data['karyawan_id'] == karyawan.id:
                    total_score = sum(
                        item['nilai_normalisasi'] * Kriteria.objects.get(nama=item['kriteria']).get_bobot()
                        for item in data['normalisasi_nilai']
                    )
                    break

            # Simpan hasil ke database
            HasilPerhitungan.objects.create(
                karyawan=karyawan,
                total_score=total_score,
                kinerja=perhitungan_fuzzy.kinerja if perhitungan_fuzzy else "Tidak tersedia"
            )

        hasil_perhitungan.append({
            'karyawan': karyawan,
            'fuzzy': perhitungan_fuzzy.kinerja if perhitungan_fuzzy else "Tidak tersedia",
            'saw_total_score': total_score,
        })

    # Urutkan hasil perhitungan berdasarkan total score dari SAW
    hasil_perhitungan.sort(key=lambda x: x['saw_total_score'], reverse=True)

    context = {
        'hasil_perhitungan': hasil_perhitungan,
    }
    return render(request, 'hasil_perhitungan.html', context)

