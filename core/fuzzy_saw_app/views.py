from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from crew.models import Crew  
from crew.forms import CrewForm
from .models import Kriteria
from .forms import KriteriaForm
from .utils import defuzzification, normalization, saw

def data_main(request):
    kriteria = Kriteria.objects.all()
    context = {
        "kriteria" : kriteria 
    }
    return render(request, 'data_main.html', context)

def data_input(request):
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

def data_edit(request, id):
    kriteria = get_object_or_404(Kriteria, id=id)
    if request.method == 'POST':
        form = KriteriaForm(request.POST, instance=kriteria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kriteria berhasil diperbarui.')
            return redirect('data_main') 
    else:
        form = CrewForm(instance=kriteria)
    context = {
        'form': form,
        'kriteria': kriteria
    }
    return render(request, 'data_edit.html', context)

def data_delete(request, id):
    kriteria = get_object_or_404(Kriteria, id=id)
    kriteria.delete()
    messages.success(request, 'Kriteria Berhasil Dihapus')
    return redirect('data_main')

def data_calculate(request):
    kriteria_list = Kriteria.objects.all()
    defuzzified_values = [defuzzification(k.K1, k.K2, k.K3) for k in kriteria_list]
    normalized_values = normalization(defuzzified_values)
    weights = [0.4, 0.3, 0.3]
    preferences = saw(normalized_values, weights)
    results = zip(kriteria_list, preferences)
    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
    return render(request, 'data_calculate.html', {'results': sorted_results})


