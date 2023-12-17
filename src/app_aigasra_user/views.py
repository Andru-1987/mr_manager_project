from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect,render
from django.core.serializers import serialize
from django.urls import reverse_lazy 
from django.http import JsonResponse
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.contrib.auth import authenticate, login


from .models import UserFile
from .models import AigasraUser , UserFile
from .forms import AigasraUserForm , AigasraUserLoginForm , AigasraUserLoginForm, AigasraUserUpdateForm




class AigasraUserLoginView(LoginView):

    http_method_names = ['get', 'post']
    template_name = 'login.html'
    extra_context = ["css/login.css"]
    success_url = reverse_lazy('novedad')



    def post(self, request, *args, **kwargs):
        form = AigasraUserLoginForm(request.POST)

        if form.is_valid():

            
            dni = form.cleaned_data['dni']
            password = form.cleaned_data['password']
            user = authenticate(request, dni=dni, password=password)
            
            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'success', "usuario":user.nombre})
            
            
            return JsonResponse({'status': 'error', 'message': 'Invalid credentials'})

        
        return JsonResponse({'status': 'error', 'message': form.errors})
    

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {"style":self.extra_context})







class AigasraUserCreateView(CreateView):
    model = AigasraUser
    form_class = AigasraUserForm
    # fields = '__all__'
    template_name = 'register.html'


    mutables: dict = {
        "telefono": {"label": "telefono", "type": "tel"},
        "celular": {"label": "celular", "type": "tel"},
        "email": {"label": "email", "type": "email"},
        "domicio_real": {"label": "domicilio real", "type": "text"},
        "password": {"label": "contraseña", "type": "password"},
        "password_2": {"label": "verificacion contraseña", "type": "password"},
    }
    inmutables: dict = {
        "nombre": {"label": "nombre", "type": "text"},
        "apellido": {"label": "apellido", "type": "text"},
        "dni": {"label": "dni", "type": "number"},
        "cuit": {"label": "cuit", "type": "number"},
        "nombre_matricula": {"label": "nombre de matricula", "type": "text"},
        "distribuidora": {"label": "distribuidora", "type": "text"},
        "dir_registracion": {"label": "dir. de registracion", "type": "text"},
        "fecha_nacimiento": {"label": "fecha de nacimiento", "type": "date"},
    }

    extra_context = {
        "style": ["css/register.css"],
        "inmutables": inmutables,
        "mutables": mutables,
    }


    def post(self, request, *args, **kwargs):
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
  
            try:
                user_form = AigasraUserForm(request.POST,request.FILES)

                print(user_form.errors)

                if user_form.is_valid():
                    
                    user = user_form.save(commit=False)
                    password = user_form.cleaned_data.get('password')
                    user.password = make_password(password)
                    user.activate_user()
                    user.save()

                    files = request.FILES.getlist('file')

                    user_files = [UserFile(user=user, file=file) for file in files]
                    UserFile.objects.bulk_create(user_files)
                    


                    return JsonResponse({'status': 'success', "ok":True,"dni":user.dni ,"message":"Se ha creado exitosamente"})
                

                    
            except Exception as e:
                print(e)
                return JsonResponse({'message': str(e)}, status=400)
        
        return JsonResponse({'error': 'Invalid request'}, status=400)
    




class AigasraUserProfileView(LoginRequiredMixin, DetailView):
    model = AigasraUser
    template_name = 'profile.html'
    context_object_name = 'user'  


    mutables: dict = {
        "telefono": {"label": "telefono", "type": "tel" },
        "celular": {"label": "celular", "type": "tel"},
        "email": {"label": "email", "type": "email"},
        "domicio_real": {"label": "domicilio real", "type": "text"},
        }
    
    inmutables: dict = {
        "nombre": {"label": "nombre", "type": "text" ,"status":"readonly" , "visbility":"hidden"},
        "apellido": {"label": "apellido", "type": "text" ,"status":"readonly" , "visbility":"hidden"},
        "dni": {"label": "dni", "type": "number" ,"status":"readonly" , "visbility":"hidden"},
        "cuit": {"label": "cuit", "type": "number" ,"status":"readonly" , "visbility":"hidden"},
        "nombre_matricula": {"label": "nombre de matricula", "type": "text" ,"status":"readonly" , "visbility":"hidden"},
        "distribuidora": {"label": "distribuidora", "type": "text" ,"status":"readonly" , "visbility":"hidden"},
        "dir_registracion": {"label": "dir. de registracion", "type": "text" ,"status":"readonly" , "visbility":"hidden"},
        "fecha_nacimiento": {"label": "fecha de nacimiento", "type": "date" ,"status":"readonly" , "visbility":"hidden"},
    }

    extra_context = {
        "style": ["css/profile.css" ,"css/profile_input.style.css"], 
        "scripts":["./js/fetch_cuotas.js","./js/fetch_cursos.js","./js/fetch_consultas.js"],
        "inmutables": inmutables,
        "mutables": mutables,
    }

    def get_object(self, queryset=None):
        return self.request.user 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = self.request.user

        for field, value in self.mutables.items():
            value.update({"value": getattr(user, field, None)})

        for field, value in self.inmutables.items():
            value.update({"value": getattr(user, field, None)})


        context["mutables"] = self.mutables
        context["inmutables"] = self.inmutables

        context["files"] = UserFile.objects.filter(user=self.request.user)

        return context
    



class AigasraUserUpdateView(UpdateView):

    model = AigasraUser
    template_name = 'update.html'
    form_class=AigasraUserUpdateForm
    
    mutables: dict = {
        "telefono": {"label": "telefono", "type": "tel"},
        "celular": {"label": "celular", "type": "tel"},
        "email": {"label": "email", "type": "email"},
        "domicio_real": {"label": "domicilio real", "type": "text"},
        "password": {"label": "contraseña", "type": "password"},
        "password_2": {"label": "verificacion contraseña", "type": "password"},
    }
    inmutables: dict = {
        "nombre": {"label": "nombre", "type": "text"},
        "apellido": {"label": "apellido", "type": "text"},
        "dni": {"label": "dni", "type": "number"},
        "cuit": {"label": "cuit", "type": "number"},
        "nombre_matricula": {"label": "nombre de matricula", "type": "text"},
        "distribuidora": {"label": "distribuidora", "type": "text"},
        "dir_registracion": {"label": "dir. de registracion", "type": "text"},
        "fecha_nacimiento": {"label": "fecha de nacimiento", "type": "date"},
    }

    extra_context = {
        "style": ["css/register.css"],
        "inmutables": inmutables,
        "mutables": mutables,
    }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        context["mutables"] = {
            key: {**value, "value": getattr(user, key, None)} 
            for key, value in self.mutables.items()
        }
        
        context["inmutables"] = {
            key: {**value, "value": getattr(user, key, None)} 
            for key, value in self.inmutables.items()
        }

        context["files"] = UserFile.objects.filter(user=user)
        return context


    def post(self, request, *args, **kwargs):

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            
            try:
                user = get_object_or_404(AigasraUser, dni=kwargs['pk'])

                user_form = AigasraUserUpdateForm(request.POST, request.FILES, instance=user)


                if user_form.is_valid():
                

                    user = user_form.save(commit=False)
                    password = user_form.cleaned_data.get('password')
                    new_dni = user_form.cleaned_data.get('dni')
                    # Update the dni field with the new value
                    user.dni = new_dni

                    if password:
                        user.password = make_password(password)

                    else:
                        del user_form.cleaned_data['password']

                    user.activate_user()
                    user.save()

                    files = request.FILES.getlist('file')
                    user_files = [UserFile(user=user, file=file) for file in files]
                    UserFile.objects.bulk_create(user_files)

                    return JsonResponse({'status': 'success', "ok": True, "dni": user.dni})

            except Exception as e:
                print(e)
                return JsonResponse({'error': str(e)}, status=400)
        
        return JsonResponse({'error': 'Invalid request'}, status=400)



# Files modifiers
    


class UserFileDeleteView(DeleteView):
    model = UserFile
    success_url = reverse_lazy('success-url')  # Replace 'success-url' with the URL to redirect after deletion

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.file.delete(save=False)  # Delete the file from storage
        self.object.delete()
        return JsonResponse({'message': 'File deleted successfully'})
