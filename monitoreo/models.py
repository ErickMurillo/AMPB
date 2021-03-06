from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class TipoOrganizacion(models.Model):
	nombre = models.CharField(max_length=250)
	slug = models.SlugField(max_length=300,editable=False)

	def __str__(self):
		return self.nombre
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(TipoOrganizacion, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name_plural = "Tipos de organización"
		verbose_name = "Tipo de organización"

class AreaTrabajo(models.Model):
	nombre = models.CharField(max_length=250)
	slug = models.SlugField(max_length=300,editable=False)

	def __str__(self):
		return self.nombre
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(AreaTrabajo, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name_plural = "Áreas de trabajo"
		verbose_name = "Área de trabajo"

class Talleres(models.Model):
	nombre = models.CharField(max_length=250)
	slug = models.SlugField(max_length=300,editable=False)

	def __str__(self):
		return self.nombre
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(Talleres, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name_plural = "Talleres"
		verbose_name = "Taller"

class TipoEmprendimiento(models.Model):
	nombre = models.CharField(max_length=250)
	slug = models.SlugField(max_length=300,editable=False)

	def __str__(self):
		return self.nombre
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(TipoEmprendimiento, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name_plural = "Tipos de Emprendimientos"
		verbose_name = "Tipo de Emprendimiento"

class Cargo(models.Model):
	nombre = models.CharField(max_length=250)
	slug = models.SlugField(max_length=300,editable=False)

	def __str__(self):
		return self.nombre
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(Cargo, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name_plural = "Cargos"
		verbose_name = "Cargo"

CHOICES_RESIDE = ((1,'Dentro'),(2,'Fuera'))

ESCOLARIDAD_CHOICES = ((1,'Primaria incompleta'),(2,'Primaria completa'),
						(3,'Secundaria incompleta'),(4,'Secundaria completa'),
						(5,'Universidad incompleta'),(6,'Universidad completa'))

TRABAJO_CHOICES = ((1,'Medio tiempo'),(2,'Tiempo completo'),(3,'Por proyectos'),(4,'No trabaja'))

SEXO_CHOICES = ((1,'Mujer'),(2,'Hombre'),(3,'Otros'))

class Participantes(models.Model):
	nombre = models.CharField(max_length=250)
	edad = models.IntegerField()
	sexo = models.IntegerField(choices=SEXO_CHOICES)
	procedencia = models.CharField(max_length=250,verbose_name='Lugar de procedencia')
	reside = models.IntegerField(verbose_name='Reside dentro o fuera de la comunidad',choices=CHOICES_RESIDE)
	nivel_escolaridad = models.IntegerField(verbose_name='Nivel de escolaridad',choices=ESCOLARIDAD_CHOICES)
	trabajo = models.IntegerField(choices=TRABAJO_CHOICES)
	organizacion = models.ForeignKey('web.Escuela', verbose_name='Organización a la que pertenece', on_delete=models.CASCADE)
	cargo = models.ForeignKey(Cargo, verbose_name='Cargo en la organización', on_delete=models.CASCADE)
	fecha = models.DateField(verbose_name='Fecha en la que se incorporó a la Escuela')
	talleres = models.ManyToManyField(Talleres, verbose_name='Talleres de la Escuela en los que ha participado')

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Participantes"
		verbose_name = "Participante"

class PerfilVocacional(models.Model):
	nombre = models.CharField(max_length=250)
	slug = models.SlugField(max_length=300,editable=False)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Perfiles vocacionales metodológico"
		verbose_name = "Perfil vocacional metodológico"
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(PerfilVocacional, self).save(*args, **kwargs)

class Formadores(models.Model):
	nombre = models.CharField(max_length=250)
	sexo = models.IntegerField(choices=SEXO_CHOICES)
	nivel_escolaridad = models.IntegerField(verbose_name='Nivel académico',choices=ESCOLARIDAD_CHOICES)
	organizacion = models.ForeignKey('web.Escuela', verbose_name='Organización forestal a la que pertenece', on_delete=models.CASCADE)
	perfil_vocacional = models.ForeignKey(PerfilVocacional, verbose_name='Perfil vocacional metodológico', on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre
	
	class Meta:
		verbose_name_plural = "Personas formadoras de formadores"
		verbose_name = "Persona formadora de formadores"
	
class Rubro(models.Model):
	nombre = models.CharField(max_length=250)
	descripcion = models.TextField()
	slug = models.SlugField(max_length=300,editable=False)

	def __str__(self):
		return self.nombre
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(Rubro, self).save(*args, **kwargs)

class Producto(models.Model):
	rubro = models.ForeignKey(Rubro, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=250)
	descripcion = models.TextField(blank=True,null=True)
	fecha = models.DateField(blank=True,null=True)
	link = models.URLField(blank=True,null=True)

	def __str__(self):
		return self.nombre
	
class FuenteFinanciamiento(models.Model):
	nombre = models.CharField(max_length=250)
	slug = models.SlugField(max_length=300,editable=False)

	def __str__(self):
		return self.nombre
	
	class Meta:
		verbose_name_plural = "Fuentes de Financiamiento"
		verbose_name = "Fuente de Financiamiento"

class HomologacionFondos(models.Model):
	rubro = models.ForeignKey(Rubro, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.rubro.nombre
	
	class Meta:
		verbose_name_plural = "Homologación de Fondos"
		verbose_name = "Homologación de Fondos"

class Presupuesto(models.Model):
	homologacion_fondos = models.ForeignKey(HomologacionFondos, on_delete=models.CASCADE)
	presupuesto = models.FloatField()
	fuente = models.ForeignKey(FuenteFinanciamiento, on_delete=models.CASCADE)
	saldo = models.FloatField(default=0)

	class Meta:
		verbose_name_plural = "Presupuesto"
		verbose_name = "Presupuesto"


MESES_CHOICES = (('Enero','Enero'),('Febrero','Febrero'),('Marzo','Marzo'),('Abril','Abril'),
				('Mayo','Mayo'),('Junio','Junio'),('Julio','Julio'),('Agosto','Agosto'),
				('Septiembre','Septiembre'),('Octubre','Octubre'),('Noviembre','Noviembre'),
				('Diciembre','Diciembre'))

class AnioEjecucion(models.Model):
	presupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE)
	anio = models.IntegerField(verbose_name='Año')

	class Meta:
		verbose_name_plural = "Años"
		verbose_name = "Año"
		

class Ejecucion(models.Model):
	anioejecucion = models.ForeignKey(AnioEjecucion, on_delete=models.CASCADE)
	mes = models.CharField(choices=MESES_CHOICES, max_length=20)
	ejecucion = models.FloatField()

	class Meta:
		verbose_name_plural = "Ejecución"
