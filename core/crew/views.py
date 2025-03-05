from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseForbidden
from .forms import CrewForm
from .models import Crew
from kriteria.decorators import check_permission 
from django import forms

@check_permission
def crew_main(request):
    crews = Crew.objects.all()
    return render(request, 'crew_main.html', {'crews': crews})

@check_permission
def crew_create(request):
    if request.method == "POST":
        form = CrewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tambah Crew Berhasil')
            return redirect('crew_main')
        else:
            messages.error(request, 'Tambah Crew Gagal')
    else:
        form = CrewForm()
    return render(request, 'crew_create.html', {'form': form})

@check_permission
def crew_edit(request, id):
    crew = get_object_or_404(Crew, id=id)
    if request.method == 'POST':
        form = CrewForm(request.POST, instance=crew)
        if form.is_valid():
            form.save()
            messages.success(request, 'Crew berhasil diperbarui.')
            return redirect('crew_main') 
    else:
        form = CrewForm(instance=crew)
    
    return render(request, 'crew_edit.html', {'form': form, 'crew': crew})

# @check_permission
# def crew_delete(request, id):
#     crew = get_object_or_404(Crew, id=id)
#     if request.method == "POST":
#         crew.delete()
#         messages.success(request, 'Crew Berhasil Dihapus')
#     return redirect('crew_main')

@check_permission
def crew_delete(request, id):
    crew = get_object_or_404(Crew, id=id)
    
    # Jika metode request adalah POST, maka lakukan penghapusan
    if request.method == "POST":
        crew.delete()
        messages.success(request, 'Crew Berhasil Dihapus')
    return redirect('crew_main')

class CrewForm(forms.ModelForm):
    class Meta:
        model = Crew
        fields = ['nama', 'posisi', 'store', 'no_hp', 'tanggal_masuk']
