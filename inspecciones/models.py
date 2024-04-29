from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=[('admin', 'Administrador'), ('user', 'Usuario')])

    def __str__(self):
        return self.user.username

    
class Elemento(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    descripcion = models.TextField()
    padre = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='elementos_hijos')

    def __str__(self):
        return self.nombre
    
class Atributo(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    descripcion = models.TextField()
    tag = models.CharField(max_length=50,unique=True)
    elemento = models.ForeignKey(Elemento, on_delete=models.CASCADE, related_name='atributos')

    def __str__(self):
        return self.tag + " || " +self._get_full_name()
    
    def _get_full_name(self):
        # Inicializar una lista para almacenar los nombres de los elementos
        full_name_parts = []

        # Obtener el primer elemento padre
        current_element = self.elemento

        # Recorrer todos los elementos padres y agregar sus nombres a la lista
        while current_element is not None:
            full_name_parts.append(current_element.nombre)
            current_element = current_element.padre

        # Invertir la lista para que los nombres se muestren desde el elemento más alto hasta el más bajo
        full_name_parts.reverse()

        # Unir los nombres con guiones para formar el nombre completo
        full_name = ' - '.join(full_name_parts)

        # Agregar el nombre del atributo al final
        full_name += f" - {self.nombre}"

        return full_name
    
    full_name = property(_get_full_name)


class Inspector(models.Model):
    nombre=models.CharField(max_length=80,unique=True)
    mail=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre

class Vulnerabilidad(models.Model):
    nombre=models.CharField(max_length=80,unique=True)
    valor=models.IntegerField()
    color = models.CharField(max_length=7, default='#000000')  # Campo para almacenar el código hexadecimal del color

    def __str__(self) -> str:
        return self.nombre
    

class ModoDeFalla(models.Model):
    nombre=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.nombre

class Inspeccion(models.Model):
    fecha=models.DateTimeField()
    inspector=models.ForeignKey(Inspector,on_delete=models.CASCADE,related_name='inspecciones')
    atributo=models.ForeignKey(Atributo,on_delete=models.CASCADE,related_name='inspecciones')
    vulnerabilidad=models.ForeignKey(Vulnerabilidad,on_delete=models.CASCADE,related_name='inspecciones')
    temperatura=models.FloatField()
    vibracion=models.FloatField()
    observacion=models.TextField()
    aviso=models.CharField(max_length=255)
    modosdefalla=models.ManyToManyField(ModoDeFalla,related_name='inspecciones',blank=True)

    def __str__(self):
        return str(self.id)


class Foto(models.Model):
    imagen = models.ImageField(upload_to='')
    inspeccion = models.ForeignKey(Inspeccion, on_delete=models.CASCADE, related_name='fotos')

    def __str__(self):
        return str(self.id)
