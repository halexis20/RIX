from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Foto

@receiver(pre_delete, sender=Foto)
def eliminar_archivo_foto(sender, instance, **kwargs):
    # Eliminar el archivo de la foto cuando se elimine la instancia de Foto
    instance.imagen.delete(save=False)