from django.db import models

# Create your models here.
class ProductoModel(models.Model):

    class OpcionesUM(models.TextChoices):
        UNIDADES = 'UN', 'UNIDADES'
        DOCENA = 'DOC', 'DOCENA'
        CIENTO = 'CI', 'CIENTO'
        MILLAR = 'MI', 'MILLAR'

    productoId = models.AutoField(primary_key=True, null=False, unique=True,db_column='id')
    productoNombre = models.CharField(max_length=45, db_column='nombre', null=False)
    productoPrecio = models.DecimalField(max_digits=5, decimal_places=2, db_column='precio')
    productoUnidadMedida = models.TextField(choices=OpcionesUM.choices, default=OpcionesUM.UNIDADES, db_column='unidad_medida')

    class Meta:
        """Link de la documentacion https://docs.djangoproject.com/en/3.2/ref/models/options/"""
        # db_table => indica el nombre de la tabla en la bd
        db_table = 'productos'
        # ordering => modifica el ordenamiento por defecto (x el id) al momento de devolver los registros
        # si queremos que sea ASC se pondra solamente el nombre del atributo, si queremos que sea DESC antes del atributo pondremos un guion (-)
        ordering = ['-productoPrecio']
        # verbose_name y verbonse_name_plural => sirven para el panel administrativo (CMS) de django
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

