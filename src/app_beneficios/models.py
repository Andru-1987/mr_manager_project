from django.db import models
from app_aigasra_user.models import AigasraUser

class Curso(models.Model):
    OPCIONES_DICTADO = (
        ('aigasra', 'Aigasra'),
        ('privado', 'Privado'),
        ('estatal', 'Estatal'),
        ('otros', 'Otros'),
    )
    
    CHOICE_STATUS = (
        ('activo','Activo' ),
        ('pospuesto','Pospuesto'),
        ('otro','Otro') 
    )

    imagen = models.ImageField(upload_to='curso_imagen/', null=True, blank=True)
    nombre = models.CharField(max_length=100, default='Curso')
    inicio = models.DateTimeField(auto_now_add=True)
    duracion = models.DurationField(default='90 days') 
    status = models.CharField(max_length=50, choices=CHOICE_STATUS, default='activo')
    dictado = models.CharField(max_length=50, choices=OPCIONES_DICTADO, default='aigasra')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    sinopsis = models.CharField(max_length=50, default='Curso generado por Aigasra.')
    detailed = models.TextField(default='')

    user = models.ManyToManyField(AigasraUser,related_name="usuarios_cursos",blank=True,null=True)

    def __str__(self) -> str:
        return f"{self.nombre}, duracion:{self.duracion} costo: {self.precio}"
    
    
    def get_fields(self):
        data = []

        for field in self.__class__._meta.fields:
            if field.verbose_name == 'imagen':
                data.append((field.verbose_name, str(self.imagen.url if self.imagen else  '')))
            else:
                data.append((field.verbose_name, field.value_from_object(self)))


        return data
    

class Normativa(models.Model):

    OPCIONES_STATUS = (
        ('actualizado', 'Actualizado'),
        ('vigente', 'Vigente'),
    )

    nombre = models.CharField(max_length=100, default='Normativa')
    normativa = models.TextField(default='')
    fecha = models.DateField()
    status = models.CharField(max_length=50, choices=OPCIONES_STATUS, default='vigente')
    explicacion = models.TextField(default='')
    link = models.URLField(default='https://www.aigasra.com.ar/educativa')

    def __str__(self) -> str:
        return f"{self.nombre}, fecha:{self.fecha} status: {self.status}"
    
    def get_fields(self):
        data = []

        for field in self.__class__._meta.fields:
            if field.verbose_name == 'imagen':
                data.append((field.verbose_name, str(self.imagen.url if self.imagen else  '')))
            else:
                data.append((field.verbose_name, field.value_from_object(self)))
        return data



class BibliotecaTecnica(models.Model):
    ARCHIVOS_PERMITIDOS = (
        ('pdf', 'PDF'),
        ('jpg', 'JPG'),
        ('png', 'PNG'),
        ('zip', 'ZIP'),
    )
    
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    short = models.CharField(max_length=50)
    full = models.TextField()
    archivos = models.FileField(upload_to='biblioteca_archivos/',null=True, blank=True)
    imagen = models.ImageField(upload_to='biblioteca_imagen/', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre}, fecha:{self.fecha}"
    

    def get_fields(self):
        data = []

        for field in self.__class__._meta.fields:
            if field.verbose_name == 'archivos':
                data.append((field.verbose_name, str(self.archivos.url if self.archivos else  '')))
            elif field.verbose_name == 'imagen':
                data.append((field.verbose_name, str(self.archivos.url if self.archivos else  '')))
            else:
                data.append((field.verbose_name, field.value_from_object(self)))

        return data