from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Historico_Imagenes(models.Model):
    cajas_teoricas = models.IntegerField(_('cajas_teoricas'), blank=False, default=1)
    cajas_practicas = models.IntegerField(_('cajas_practicas'), blank=False, default=1)
    imagen_sin_analizar = models.CharField(_("imagen_sin_analizar"), max_length=100)
    imagen_analizada = models.CharField(_("imagen_sin_analizar"), max_length=100)
    porcentaje = models.FloatField(_('porcentaje'), blank=False, default=1)

    class Meta:
        db_table = 'Historico_Imagenes'
        ordering = ['-id']
        verbose_name_plural = 'Historico_Imagenes'