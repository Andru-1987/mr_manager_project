from django.views.generic import ListView , DetailView
from django.http import JsonResponse
from .models import Contacto , Novedad

# Create your views here.

GLOBAL_PAGINATION = 4

class Autoridades(ListView):
    model = Contacto
    paginate_by = GLOBAL_PAGINATION
    template_name = "autoridades.html"
    extra_context = {
        "style": ["css/login.css"],
        "page":"autoridades"
        }
    


class AutoridadesDetail(DetailView):
    model = Contacto 

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()  
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def render_to_response(self, context, **response_kwargs):
        data = dict(Contacto.get_fields(self.object))
        return JsonResponse(data)




class Novedades(ListView):
    model = Novedad
    template_name = "novedades.html"
    paginate_by = GLOBAL_PAGINATION
    extra_context = {
        "style": ["css/login.css"],
        "page":"novedades"
        }
    


class NovedadesDetail(DetailView):
    model = Novedad 

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()  
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def render_to_response(self, context, **response_kwargs):
        data = dict(Novedad.get_fields(self.object))
        return JsonResponse(data)
