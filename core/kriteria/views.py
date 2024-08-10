from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Kriteria
from .forms import KriteriaForm
from .decorators import check_permission

@login_required
@check_permission
def kriteria_list(request):
    kriteria = Kriteria.objects.all()
    context = {
        'kriteria_list': kriteria
    }
    return render(request, 'kriteria_list.html', context)

@login_required
@check_permission
def kriteria_create(request):
    if request.method == 'POST':
        form = KriteriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kriteria berhasil ditambahkan.')
            return redirect('kriteria_list')
        else:
            messages.error(request, 'Terjadi kesalahan pada form.')
    else:
        form = KriteriaForm()
    
    context = {
        'form': form
    }
    return render(request, 'kriteria_create.html', context)

@login_required
@check_permission
def kriteria_edit(request, id):
    kriteria = get_object_or_404(Kriteria, id=id)
    if request.method == 'POST':
        form = KriteriaForm(request.POST, instance=kriteria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kriteria berhasil diperbarui.')
            return redirect('kriteria_list')
        else:
            messages.error(request, 'Terjadi kesalahan pada form.')
    else:
        form = KriteriaForm(instance=kriteria)
    
    context = {
        'form': form,
        'kriteria': kriteria
    }
    return render(request, 'kriteria_edit.html', context)

@login_required
@check_permission
def kriteria_delete(request, id): 
    kriteria = get_object_or_404(Kriteria, id=id)
    if request.method == 'POST':
        kriteria.delete()
        messages.success(request, 'Kriteria berhasil dihapus.')
    return redirect('kriteria_list')
