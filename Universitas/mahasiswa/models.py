from django.db import models

# Create your models here.


from django.db import models

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=10, primary_key=True)
    nama = models.CharField(max_length=255)
    jurusan = models.CharField(max_length=255)
    angkatan = models.IntegerField()
