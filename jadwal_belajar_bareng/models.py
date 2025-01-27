from django.db import models
import datetime
from django.utils.timezone import now

CHOICES = (
  ("Alin","Aljabar Linear"),
  ("MPPI","Metodologi Penelitian dan Penulisan Ilmiah"),
  ("PBP","Pemrograman Berbasis Platform"),
  ("SOSI","Sistem Operasi untuk Sistem Informasi"),
  ("SDA","Struktur Data & Algoritma"),
)

PRIORITY = (
  ("Tinggi","Tinggi"),
  ("Sedang","Sedang"),
  ("Rendah","Rendah"),
)

class JadwalBelajarBareng(models.Model):
  def __str__(self): 
    return self.Topik
  Prioritas = models.TextField(max_length = 15, choices=PRIORITY)
  Matkul = models.TextField(max_length = 150, choices=CHOICES)
  Waktu = models.DateTimeField()
  Topik = models.CharField(max_length = 150)
  Informasi = models.TextField()
  Link = models.URLField(max_length = 200)