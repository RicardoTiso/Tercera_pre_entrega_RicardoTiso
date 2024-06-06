from django.db import models

# Create your models here.

class ClasesAlumnos(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=30)
    clase= models.IntegerField()
    fechaDeClase= models.DateField()
    def __str__(self):
        return f'Alumno: {self.nombre} {self.apellido} - Clase:{self.clase} - fecha: {self.fechaDeClase}'

class RegistroInstructores(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=30)
    clase= models.IntegerField()
    titulo=models.CharField(max_length=30)
    reseña = models.TextField()
    fechaDeClase= models.DateField()
    def __str__(self):
        return f'Instructor: {self.nombre} {self.apellido} - Titulo de la clase: {self.titulo}, a dictar el dia {self.fechaDeClase} [mas...]'

class Alumnos(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField(null=True)
    def __str__(self):
        return f'Alumno: {self.nombre} {self.apellido} - Email: {self.email}'

class Instructor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    clase= models.CharField(max_length=30)
    def __str__(self):
        return f'Profesor: {self.nombre} {self.apellido} - Email: {self.email} - Perfecciona en:{self.clase}'

class Clases(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=30)
    fechaDeClase= models.DateField()
    clase= models.IntegerField()
    def __str__(self):
        return f'Clase:{self.clase} - Fecha de entrega: {self.fechaDeClase} - Instructor: {self.nombre} {self.apellido}'
    
class Desafios(models.Model):
    desafio= models.CharField(max_length=30)
    fechaLimite= models.DateField()
    completado= models.BooleanField()
    def Estado(self):
        if self.completado:
            return 'Desafio Completado'
        else:
            return 'No Completado'
    def __str__(self):
        return f'Desafio: {self.desafio} - Fecha de entrega: {self.fechaLimite} - Estado: {self.Estado()}'
