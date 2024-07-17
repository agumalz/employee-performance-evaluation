from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . forms import CrewForm
from . models import Job, Crew

# Create your views here.

def crew_main(request):
    crews = Crew.objects.all()
    context = {
        'crews' : crews
    }
    return render(request, 'crew_main.html', context)

def crew_create(request):
    if request.method == "POST":
        form = CrewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tambah Crew Berhasil')
            return redirect('crew_main')
        else:
            messages.error(request, 'Tambah Crew Gagal')
            # return render(request, 'crew_create.html', {'form' : form})
    else:
        form = CrewForm()
    return render(request, 'crew_create.html', {'form': form})

def crew_edit(request, id):
    crews = get_object_or_404(Crew, id=id)
    if request.method == 'POST':
        form = CrewForm(request.POST, instance=crews)
        if form.is_valid():
            form.save()
            messages.success(request, 'Crew berhasil diperbarui.')
            return redirect('crew_main') 
    else:
        form = CrewForm(instance=crews)
    context = {
        'form': form,
        'crews': crews
    }
    return render(request, 'crew_edit.html', context)

def crew_delete(request, id):
    crew = get_object_or_404(Crew, id=id)
    crew.delete()
    messages.success(request, 'Crew Berhasil Dihapus')
    return redirect('crew_main')