from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField

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

class Historic_Vehicles_detected(models.Model):
    device_id = models.CharField(_("device_id"), blank=False, max_length=50)
    time = models.DateTimeField(_("time"), auto_now=False, auto_now_add=True)
    image = models.CharField(_("image"), max_length=100)
    vehicles_detected = models.IntegerField(_("vehicles_detected"))
    awsRekognition_response = JSONField(_("awsRekognition_response"))

    class Meta:
        db_table = 'Historic_Vehicles_detected'
        ordering = ['-id']
        verbose_name_plural = 'Historic_Vehicles_detected'