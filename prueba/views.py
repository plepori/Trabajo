from django.shortcuts import render, get_object_or_404
from prueba.models import Familiar
from prueba.forms import Buscar, FamiliarForm 
from django.views import View  
from django.views.generic import ListView, CreateView, DeleteView, UpdateView  # <----- NUEVO IMPORT


# Create your views here.

def inicio(request, nombre):
    
    return render(request, "prueba/test.html", {"nombre":nombre})

def listar_familia(request):
    fam = Familiar.objects.all()
    return render(request, "prueba/listar.html",{"fam":fam})

class BuscarFamiliar(View): #creamos clase buscar y heredamos View

    form_class = Buscar  # instanciamos buscar que viene del form, 
    template_name = 'prueba/buscar.html' # definimos la ruta en template_name
    initial = {"nombre":""}  # definimos sin valor la clave

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, 'prueba/buscar.html', {'form':form})

    def post(self, request):
        form = self.form_class(request.POST) # form instancia clase Buscar del formulario, con la respuesta de la web
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all()
            form = self.form_class(initial=self.initial)
            return render(request,'prueba/buscar.html', {'form':form, 'lista_familiares':lista_familiares})
        
        return render(request, 'prueba/buscar.html', {'form':form})


class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'prueba/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'prueba/actualizar_familiar.html'
  success_template = 'prueba/exito.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar,'pk':pk})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form,'familiar': familiar, 'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})


class Borrar(View):
  form_class = FamiliarForm
  template_name = 'prueba/borrar.html'
  success_template = 'prueba/exito.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      
      return render(request, self.template_name, {'form':form,'familiar': familiar,'pk':pk})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      familiar = Familiar.objects.get(id=pk)
      familiar.delete()
      form = self.form_class(request.POST)
      return render(request, 'prueba/mostrar.html', {"form": form, "pk":pk,"familiar":familiar})

class FamiliarList(ListView):
  model = Familiar

class FamiliarCrear(CreateView):
    model = Familiar
    success_url = "/panel-familia"
    fields = ["nombre", "direccion", "dni"]


class FamiliarBorrar(DeleteView):
  model = Familiar
  success_url = "/panel-familia"


class FamiliarActualizar(UpdateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "dni"]