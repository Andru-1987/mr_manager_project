from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView


class LandingPage(TemplateView):
    template_name = "index.html"
    extra_context = {"style": ["css/style.css"]}


class LoginPage(TemplateView):
    template_name = "login.html"

    extra_context = {"style": ["css/login.css"]}


class RegisterPage(TemplateView):
    template_name = "register.html"

    mutables: dict = {
        "telefono": {"label": "telefono", "type": "tel"},
        "celular": {"label": "celular", "type": "tel"},
        "email": {"label": "email", "type": "email"},
        "domicio real": {"label": "domicilio real", "type": "text"},
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
        "fecha_nacimiento": {"label": "fecha de nacimiento", "type": "text"},
    }

    extra_context = {
        "style": ["css/register.css"],
        "inmutables": inmutables,
        "mutables": mutables,
    }


from django.shortcuts import render

class Custom404View(View):
    def dispatch(self, request, exception):
        return render(request, '404.html', status=404)
