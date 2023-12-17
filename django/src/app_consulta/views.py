from django.views import View
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.db.models import Count

from .models import Consulta , ArchivoConsulta
from .forms import ConsultaForm



class ConsultaCreateView(CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = "consulta_form.html"
    extra_context = {"style": ["css/consulta.css"]}
    success_url = reverse_lazy('profile')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        form.instance.usuario_consulta = self.request.user
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        try:
            consulta_form = ConsultaForm(request.POST, request.FILES)
            response = super().form_valid(consulta_form)

            if consulta_form.is_valid():
                consulta = consulta_form.save(commit=False)
                consulta.usuario_consulta = self.request.user
                consulta.save()

                archivos = request.FILES.getlist('archivo')
            
                consulta_files = [
                    ArchivoConsulta(consulta=consulta, archivo=file) for file in archivos
                ]
                ArchivoConsulta.objects.bulk_create(consulta_files)
                return response
                
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)



class ConsultaListView(LoginRequiredMixin, View):
    
    cols = [
            "titulo_consulta"
        ,   "fecha_consulta"
        ,   "temas_relacionados"
        ,   "receptor_consulta"
        ,   "consulta_texto"
    ]

    def get(self, request, *args, **kwargs):
        user = request.user
        
        consulta_usuario_logged = Consulta.objects.filter(usuario_consulta=user)
        cantidad_consultas = consulta_usuario_logged.count()
        consultas = consulta_usuario_logged\
            .annotate(
            total_files=Count('archivos_consultas')
        )


        consultas = Consulta.objects.filter(usuario_consulta=user).annotate(
            total_files=Count('archivos_consultas'),
        )

        consultas_data = []
        for consulta in consultas:
            archivos = consulta.archivos_consultas.all()
            file_info = []
            for archivo in archivos:
                file_info.append({
                    "path": archivo.archivo.url,  
                    "name": archivo.filename(),  
                    "type": archivo.tipo_archivo(),
                })

            consultas_data.append({
                "id": consulta.id,
                "titulo_consulta": consulta.titulo_consulta,
                "total_files": consulta.total_files,
                "fecha_consulta": consulta.fecha_consulta.strftime('%Y-%m-%d %H:%M:%S'),
                "temas_relacionados": consulta.temas_relacionados,
                "receptor_consulta": consulta.receptor_consulta.nombre,
                "consulta_texto":consulta.consulta_texto,
                "file_info": file_info,
            })


        
        return JsonResponse({
            "data":consultas_data,
            "total_consultas":cantidad_consultas
            }, safe=False)
