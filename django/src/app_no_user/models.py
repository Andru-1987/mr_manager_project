from django.db import models
from django.db import models
from django.utils import timezone

# Create your models here.

class Contacto(models.Model):

    class Meta:
        db_table = "contacto"

    CARGO_CHOICES = [
        ('director', 'Director'),
        ('secretario', 'Secretario'),
        ('subsecretario', 'Subsecretario'),
        ('editor','Editor'),
        ('tesorero','Tesorero'),
        ('otro','Otro')
    ]
    
    TITULO_CHOICES = [
        ('licenciado', 'Licenciado'),
        ('tecnico', 'Técnico'),
        ('arquitecto', 'Arquitecto'),
        ('doctor', 'Doctor'),
        ('master', 'Máster'),
        ('ingeniero', 'Ingeniero'),
        ('otro', 'Otro'),
    ]
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='contacto_images/',blank=True,null=True)
    cargo = models.CharField(max_length=20, choices=CARGO_CHOICES)
    titulo = models.CharField(max_length=20, choices=TITULO_CHOICES)
    biografia = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def get_fields(self):
        data = []

        for field in self.__class__._meta.fields:
            if field.verbose_name == 'imagen':
                data.append((field.verbose_name, str(self.imagen.url if self.imagen else  '')))
            else:
                data.append((field.verbose_name, field.value_from_object(self)))


        return data


class Novedad(models.Model):
    class Meta:
        db_table = "novedad"

    corto = models.CharField(max_length=100,default="Articulo de Aigasra")
    largo = models.CharField(max_length=255)
    edicion = models.DateTimeField(default=timezone.now)
    creado = models.ForeignKey(Contacto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='novedades_images/')
    bio = models.TextField()

    def __str__(self):
        return self.corto
    
    def get_fields(self):
        data = []

        for field in self.__class__._meta.fields:
            if field.verbose_name == 'imagen':
                data.append((field.verbose_name, str(self.imagen.url if self.imagen.url else  '')))
            elif field.verbose_name == 'creado':
                data.append((field.verbose_name, str(self.creado) ))
            else:
                data.append((field.verbose_name, field.value_from_object(self)))


        return data
