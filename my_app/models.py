from django.db import models

# Create your models here.
# los modelos sireven para crear tablas provienentes de una base de datos 
class Project(models.Model):
    name = models.CharField(max_length=200)
    
class Task(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
