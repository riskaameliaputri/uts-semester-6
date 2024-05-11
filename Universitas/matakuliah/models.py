from django.db import models

class Matakuliah(models.Model):
    kode_matkul = models.CharField(max_length=10, primary_key=True)
    nama_matkul = models.CharField(max_length=255)
    sks = models.IntegerField()
    dosen_pengampu = models.CharField(max_length=255)
