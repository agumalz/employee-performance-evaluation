from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from crew.models import Crew  
from crew.forms import CrewForm
from .models import Kriteria
from .forms import KriteriaForm
from .utils import defuzzification, normalization, saw
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

@login_required
def data_main(request):
    if request.user.profile.position == 'crew':
        return HttpResponseForbidden("Anda tidak memiliki akses ke halaman ini.")
    
    kriteria = Kriteria.objects.all()
    context = {
        "kriteria" : kriteria 
    }
    return render(request, 'data_main.html', context)

@login_required
def data_input(request):
    if request.user.profile.position == 'crew':
        return HttpResponseForbidden("Anda tidak memiliki akses ke halaman ini.")
    
    if request.method == 'POST':
        form = KriteriaForm(request.POST)
        if form.is_valid():
            kriteria_instance = form.save(commit=False)
            kriteria_instance.crew_name = request.POST.get('crew_name')
            kriteria_instance.save()
            messages.success(request, 'Data berhasil disimpan.')
            return redirect('data_calculate')
        else:
            messages.error(request, 'Terjadi kesalahan pada form.')
    else:
        form = KriteriaForm()
    return render(request, 'data_input.html', {'form': form})

@login_required
def data_edit(request, id):
    if request.user.profile.position == 'crew':
        return HttpResponseForbidden("Anda tidak memiliki akses ke halaman ini.")
    
    kriteria = get_object_or_404(Kriteria, id=id)
    crew = kriteria.crew
    if request.method == 'POST':
        form = KriteriaForm(request.POST, instance=kriteria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kriteria berhasil diperbarui.')
            return redirect('data_main')
    else:
        form = KriteriaForm(instance=kriteria)
    
    context = {
        'form': form,
        'kriteria': kriteria,
        'crew': crew
    }
    return render(request, 'data_edit.html', context)

@login_required
def data_delete(request, id):
    if request.user.profile.position == 'crew':
        return HttpResponseForbidden("Anda tidak memiliki akses ke halaman ini.")
    
    kriteria = get_object_or_404(Kriteria, id=id)
    kriteria.delete()
    messages.success(request, 'Kriteria Berhasil Dihapus')
    return redirect('data_main')

@login_required
def data_calculate(request):
    kriteria_list = Kriteria.objects.all()
    defuzzified_values = [defuzzification(k.K1, k.K2, k.K3) for k in kriteria_list]
    normalized_values = normalization(defuzzified_values)
    weights = [0.4, 0.3, 0.3]
    preferences = saw(normalized_values, weights)
    results = zip(kriteria_list, preferences)
    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
    return render(request, 'data_calculate.html', {'results': sorted_results})

@login_required
def visualisasi_data(request):
    kriteria_list = Kriteria.objects.all()
    kriteria_names = [k.crew.crew_name for k in kriteria_list]
    kriteria_k1 = [k.K1 for k in kriteria_list]
    kriteria_k2 = [k.K2 for k in kriteria_list]
    kriteria_k3 = [k.K3 for k in kriteria_list]
    
    context = {
        'kriteria_names': kriteria_names,
        'kriteria_k1': kriteria_k1,
        'kriteria_k2': kriteria_k2,
        'kriteria_k3': kriteria_k3,
    }
    return render(request, 'visualisasi_data.html', context)

