from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=2,
                help_text='Código de 2 letras del país, ejemplo : Nicaragua (ni)')

    class Meta:
        verbose_name_plural = "Países"

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    pais = models.ForeignKey(Pais,on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Departamentos"
        ordering = ['nombre']

class Municipio(models.Model):
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return '%s - %s' % (self.departamento.nombre, self.nombre)

    class Meta:
        verbose_name_plural = "Municipios"
        ordering = ['departamento__nombre', 'nombre']