from datetime import date,timezone,timedelta
from random import choice
from .models import Normativa , Curso , BibliotecaTecnica

def populate():
    for i in range(20):
        normativa = Normativa.objects.create(
            nombre=f'Normativa {i+1}',
            normativa=f'Contenido de la normativa {i+1}',
            fecha=date.today(),  # Set the date as needed
            status=choice(['actualizado', 'vigente']),
            explicacion=f'Explicación de la normativa {i+1}',
            link=f'https://www.aigasra.com.ar/normativa/{i+1}'
        )

    for i in range(20):
        biblioteca = BibliotecaTecnica.objects.create(
            nombre=f'Biblioteca {i+1}',
            fecha=date.today(),  # Set the date as needed
            short=f'Short description {i+1}',
            full=f'Full description {i+1}',
            # Set files or images as needed
        )

    for i in range(20):
        curso = Curso(
            nombre=f'Curso {i+1}',
            duracion=timedelta(days=90),  # Set the duration as needed
            status='activo',  # Set the status as needed
            precio=100.00 * (i+1),  # Set the price as needed
            sinopsis=f'Sinopsis del curso {i+1}',
            detailed=f'Detalles del curso {i+1}'
            # Add other fields with appropriate values
        )

        curso.save()
        normativa.save()
        biblioteca.save()


if __name__ == '__main__':
    populate()
