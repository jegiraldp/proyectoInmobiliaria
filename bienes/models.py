from django.db import models

class persona(models.Model):
    documento=models.IntegerField()
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    edad = models.IntegerField(default=0)

    def __str__(self):
        return (self.nombres+" "+self.apellidos)
