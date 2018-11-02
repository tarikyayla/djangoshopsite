from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.SatisKategorileri)
admin.site.register(models.Urunler)
admin.site.register(models.Cart)