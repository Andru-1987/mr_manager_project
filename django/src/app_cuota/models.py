from django.db import models
from django.utils import timezone
from app_aigasra_user.models import AigasraUser

class Cuota(models.Model):
    MESES = [
        (1, 'Enero'),
        (2, 'Febrero'),
        (3, 'Marzo'),
        (4, 'Abril'),
        (5, 'Mayo'),
        (6, 'Junio'),
        (7, 'Julio'),
        (8, 'Agosto'),
        (9, 'Septiembre'),
        (10, 'Octubre'),
        (11, 'Noviembre'),
        (12, 'Diciembre'),
    ]

    MONEDAS = [
        ('ARS', 'Pesos argentinos'),
        ('USD', 'Dólares estadounidenses'),
        ('BRL', 'Reales brasileños'),
    ]

    mes_cuota = models.IntegerField(choices=MESES, default=timezone.now().strftime('%B').lower())
    anno_cuota = models.IntegerField(default=timezone.now().year)
    mes_cuota_vencimiento = models.IntegerField(choices=MESES)
    anno_cuota_vencimiento = models.IntegerField(default=timezone.now().year)
    descripcion = models.CharField(max_length=255,default=f"Cuota Aigasra Sociedad")
    valor_cuota = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    moneda = models.CharField(max_length=15, choices=MONEDAS, default='ARS')
    usuario = models.ForeignKey(AigasraUser, on_delete=models.CASCADE, blank=True,null=True)

    class Meta:
        verbose_name = 'Cuota'
        verbose_name_plural = 'Cuotas'


    def __str__(self):
        return f"Cuota {self.id} - {self.mes_cuota} {self.anno_cuota} - Vencimiento: {self.mes_cuota_vencimiento} {self.anno_cuota_vencimiento}"

