import os
from pathlib import Path
from django.db import models
from django.utils import timezone
from app_aigasra_user.models import AigasraUser



class Consulta(models.Model):
    usuario_consulta = models.ForeignKey(AigasraUser, on_delete=models.CASCADE, related_name='consultas_realizadas')
    receptor_consulta = models.ForeignKey(AigasraUser, on_delete=models.CASCADE, related_name='consultas_recibidas', limit_choices_to={'staff': True})
    titulo_consulta = models.CharField(max_length=255)
    fecha_consulta = models.DateTimeField( editable=False, auto_now_add=True)
    temas_relacionados = models.CharField(max_length=255)
    email_contacto = models.EmailField(verbose_name="Email de contacto",blank=True,null=True)
    consulta_texto = models.TextField()

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        
    def __str__(self):
        return f"{self.titulo_consulta} - {self.usuario_consulta.nombre}"



class ArchivoConsulta(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, related_name='archivos_consultas')
    archivo = models.FileField(upload_to='consultas_archivos/')

    def __str__(self):
        return f"Archivo: {self.tipo_archivo()} : {self.consulta.titulo_consulta}"
    
    def filename(self):
        path = Path(self.archivo.name)
        return f"{path.stem}"

    def tipo_archivo(self):
        file_extension = os.path.splitext(self.archivo.name)[1]
    
        if file_extension.lower() in ['.pdf']:
            return 'PDF'
        elif file_extension.lower() in ['.doc', '.docx']:
            return 'Word Document'
        elif file_extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
            return 'Image'
        else:
            return 'Desconocido'