from django.db import models
from django.utils import timezone


class Post(models.Model):
    penulis = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    tanggal_pembuatan = models.DateTimeField(
            default=timezone.now)
    tanggal_publikasi = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.tanggal_publikasi = timezone.now()
        self.save()

    def __str__(self):
        return self.judul
