from django.db import models
from django.contrib.auth.models import User

class Kutaa(models.Model):
    # Filannoo 1-12 qopheessuu
    KUTAA_CHOICES = [(i, f"Kutaa {i}") for i in range(1, 13)]
    
    lakk_kutaa = models.IntegerField(
        choices=KUTAA_CHOICES, 
        unique=True, 
        verbose_name="Lakkoofsa Kutaa"
    )
    gaffii = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Kutaa {self.lakk_kutaa}"

class Barataa(models.Model):
    maqaa_guutuu = models.CharField(max_length=100)
    kutaa = models.ForeignKey(Kutaa, on_delete=models.CASCADE)
    maqaa_maatii = models.ForeignKey(User, on_delete=models.CASCADE)
    bilbila_maatii = models.CharField(max_length=15)

    def __str__(self):
        return self.maqaa_guutuu