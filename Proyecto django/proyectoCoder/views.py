from django.shortcuts import render, redirect
from proyectoCoder.Models import Casa
from proyectoCoder.forms.Forms import CasaFormulario

def crear_casa(request):
    if request.method == 'POST':
        casa_form = CasaFormulario(request.POST)
        if casa_form.is_valid():
            
            nombre = casa_form.cleaned_data['nombre']
            direccion = casa_form.cleaned_data['direccion']
            cantidad_habitantes = casa_form.cleaned_data['cantidad_habitantes']
            barrio = casa_form.cleaned_data['barrio']
            
            Casa.objects.create(
                nombre=nombre,
                direccion=direccion,
                cantidad_habitantes=cantidad_habitantes,
                barrio=barrio
            )
            Casa.save()
            return redirect('login.html')
    else:
        casa_form = CasaFormulario()
    
    return render(request, 'guardar_casa.html', {'casa_form': casa_form})
