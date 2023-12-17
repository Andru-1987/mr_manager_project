from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cuota



class CuotaListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        cuotas = Cuota.objects.filter(usuario=user)

        cuotas_data = list(cuotas.values(
            'mes_cuota', 'anno_cuota', 'mes_cuota_vencimiento',
            'anno_cuota_vencimiento', 'descripcion', 'valor_cuota', 'moneda'
        ))

        return JsonResponse(cuotas_data, safe=False)
