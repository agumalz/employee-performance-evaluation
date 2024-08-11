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
        nilai_kriteria = []
        for kriteria in kriteria_list:
            try:
                nilai = KaryawanKriteria.objects.get(karyawan=karyawan, kriteria=kriteria).nilai
            except KaryawanKriteria.DoesNotExist:
                nilai = None
            nilai_kriteria.append({
                'kriteria': kriteria.nama,
                'nilai': nilai
            })
        penilaian_data.append({
            'karyawan': karyawan.nama,
            'karyawan_id': karyawan.id,
            'nilai_kriteria': nilai_kriteria
        })

    context = {
        'penilaian_data': penilaian_data,
        'kriteria_list': kriteria_list,
    }

    return render(request, 'karyawan_kriteria_list.html', context)

def karyawan_kriteria_create(request):
    if request.method == 'POST':
        form = KaryawanKriteriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Penilaian karyawan berhasil disimpan.')
            return redirect('karyawan_kriteria_list')
    else:
        form = KaryawanKriteriaForm()

    return render(request, 'karyawan_kriteria_form.html', {'form': form})

def karyawan_kriteria_edit(request, karyawan_id):
    karyawan = get_object_or_404(Crew, id=karyawan_id)
    kriteria_list = Kriteria.objects.all()
    
    if request.method == 'POST':
        form = KaryawanKriteriaForm(request.POST)
        if form.is_valid():
            for kriteria in kriteria_list:
                nilai = form.cleaned_data.get(f'nilai_{kriteria.id}')
                if nilai is not None:
                    KaryawanKriteria.objects.update_or_create(
                        karyawan=karyawan,
                        kriteria=kriteria,
                        defaults={'nilai': nilai}
                    )
            messages.success(request, 'Penilaian karyawan berhasil diperbarui.')
            return redirect('karyawan_kriteria_list')
    else:
        form = KaryawanKriteriaForm(initial={'karyawan': karyawan})
        for kriteria in kriteria_list:
            try:
                nilai = KaryawanKriteria.objects.get(karyawan=karyawan, kriteria=kriteria).nilai
                form.fields[f'nilai_{kriteria.id}'].initial = nilai
            except KaryawanKriteria.DoesNotExist:
                pass

    return render(request, 'karyawan_kriteria_form.html', {'form': form})

def karyawan_kriteria_delete(request, karyawan_id):
    karyawan = get_object_or_404(Crew, id=karyawan_id)
    KaryawanKriteria.objects.filter(karyawan=karyawan).delete()
    messages.success(request, 'Penilaian karyawan berhasil dihapus.')
    return redirect('karyawan_kriteria_list')
