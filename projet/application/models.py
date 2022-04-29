from django.db import models

# Create your models here.


class Avion(models.Model):
    nom = models.CharField(max_length=100)
    fabriquant = models.CharField(max_length = 100)
    date_production = models.DateField(blank=True, null = True)
    nombre_avion = models.IntegerField(blank=False)
    resume = models.TextField(null = True, blank = True)
    def __str__(self):
        chaine = f"{self.nom} produit par {self.fabriquant} avec {self.nombre_avion} exemplaires"
        return chaine

    def dico(self):
        return {"nom" : self.nom, "fabriquant" : self.fabriquant, "date_production" : self.date_production, "nombre_avion" : self.nombre_avion, "resume" : self.resume }