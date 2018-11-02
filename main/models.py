from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SatisKategorileri(models.Model):
    id = models.AutoField(primary_key=True)
    kategoriName = models.CharField(max_length=100)

    def __str__(self):
        return self.kategoriName

class Urunler(models.Model):
    id = models.AutoField(primary_key=True)
    kategori = models.ForeignKey(SatisKategorileri,on_delete=models.CASCADE)
    urun_gorseli = models.CharField(max_length=150)
    urun_ismi = models.CharField(max_length=100)
    fiyat = models.FloatField(max_length=50)
    def __str__(self):
        return self.urun_ismi

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    urun_id = models.ForeignKey(Urunler,on_delete=models.CASCADE)
    kullanici_id = models.ForeignKey(User,on_delete=models.CASCADE)
    fiyat = models.FloatField(max_length=150)
    def __str__(self):
        return str(self.urun_id)