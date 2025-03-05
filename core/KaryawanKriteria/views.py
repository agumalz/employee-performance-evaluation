from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import KaryawanKriteriaForm
from .models import KaryawanKriteria
from crew.models import Crew
from kriteria.models import Kriteria

def karyawan_kriteria_list(request):
    karyawan_list = Crew.objects.all()
    kriteria_list = Kriteria.objects.all()

    penilaian_data = []
    for karyawan in karyawan_list:
        nilai_kriteria = [
            {'kriteria': kriteria.nama, 'nilai': KaryawanKriteria.objects.filter(karyawan=karyawan, kriteria=kriteria).first().nilai if KaryawanKriteria.objects.filter(karyawan=karyawan, kriteria=kriteria).exists() else None}
            for kriteria in kriteria_list
        ]
        penilaian_data.append({'karyawan': karyawan.nama, 'karyawan_id': karyawan.id, 'nilai_kriteria': nilai_kriteria})

    return render(request, 'karyawan_kriteria_list.html', {'penilaian_data': penilaian_data, 'kriteria_list': kriteria_list})

def karyawan_kriteria_create(request):
    if request.method == 'POST':
        form = KaryawanKriteriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Penilaian karyawan berhasil disimpan.')
            return redirect('karyawan_kriteria_list')
    else:
        form = KaryawanKriteriaForm()

    return render(request, 'karyawan_kriteria_form.html', {'form': form, 'is_edit': False})

def karyawan_kriteria_edit(request, karyawan_id):
    karyawan = get_object_or_404(Crew, id=karyawan_id)

    if request.method == 'POST':
        form = KaryawanKriteriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Penilaian karyawan berhasil diperbarui.')
            return redirect('karyawan_kriteria_list')
    else:
        initial_data = {'karyawan': karyawan}
        for kriteria in Kriteria.objects.all():
            nilai = KaryawanKriteria.objects.filter(karyawan=karyawan, kriteria=kriteria).first()
            if nilai:
                initial_data[f'nilai_{kriteria.id}'] = nilai.nilai

        form = KaryawanKriteriaForm(initial=initial_data)

    return render(request, 'karyawan_kriteria_form.html', {'form': form, 'is_edit': True})

def karyawan_kriteria_delete(request, karyawan_id):
    karyawan = get_object_or_404(Crew, id=karyawan_id)
    KaryawanKriteria.objects.filter(karyawan=karyawan).delete()
    messages.success(request, 'Penilaian karyawan berhasil dihapus.')
    return redirect('karyawan_kriteria_list')
