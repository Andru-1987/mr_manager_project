from .models import Curso , Normativa , BibliotecaTecnica
from .builder_util import  Builder

from django.shortcuts import get_object_or_404
from django.views import View
from django.http import JsonResponse
from .models import Curso


curso = Builder(Curso)
curso = curso.add_list_values("curso.html",{"page":"cursos"})
curso = curso.add_cols_json(
            "nombre"
            ,"inicio"
            ,"status"
            ,"dictado"
        )
curso = curso.detail_update_template()\
        .detail_page()

normativa = Builder(Normativa)
normativa = normativa.add_list_values("normativa.html" ,{"page":"normativas"}).detail_update_template().detail_page()

biblioteca_tecnica = Builder(BibliotecaTecnica)
biblioteca_tecnica = biblioteca_tecnica.add_list_values("biblioteca.html" ,{"page":"biblioteca"})
biblioteca_tecnica = biblioteca_tecnica.detail_update_template().detail_page()




class JoinCursoView(View):
    def post(self, request, curso_id):
        user = request.user 
        
        curso = get_object_or_404(Curso, id=curso_id)
        
        # Check if the user is already in the curso
        if user in curso.user.all():
            return JsonResponse({'message': 'Ya se encuentra inscripto'})
        
        curso.user.add(user)
        
        return JsonResponse({'message': 'Genial! gracias por inscribirte'})

    def delete(self, request, curso_id):
        user = request.user  # Assuming you have user authentication enabled
        
        curso = get_object_or_404(Curso, id=curso_id)
        
        # Check if the user is enrolled in the curso before removing
        if user not in curso.user.all():
            return JsonResponse({'message': 'No te encontras inscripto'})
        
        curso.user.remove(user)
        
        return JsonResponse({'message': 'Ya estás dado baja, gracias!'})
