# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User

# Modelo
def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.categoria, filename)

class Usuario(models.Model):
    #Tupla de opciones género
    OP_GENERO = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    )

    #Tupla de opciones tipo usuario
    OP_TIPO = (
        ('I', 'Institución'),
        ('P', 'Persona'),
    )
    
    iduser = models.OneToOneField(User)
    nombre = models.CharField(max_length = 50)
    apellido_pat = models.CharField(max_lenght = 50)
    apellido_mat = = models.CharField(max_lenght = 50)
    #En la base de datos se guardará la opción como H o M
    genero = models.CharField(max_lenght = 1, choices = OP_GENERO)
    año_nac = models.DateField()
    email = models.CharField(max_lenght = 50)
    no_tel = models.CharField(max_lenght = 50)
    direccion = models.CharField(max_lenght = 100)
    biografia = models.CharField(max_lenght = 300)
    #En la base de datos se guardará la opción como I o P
    tipo_user = models.CharField(max_lenght = 1, choices = OP_TIPO)
    foto_perfil = models.FileField(upload_to=user_directory_path)

    def __unicode__(self):
        return self.nombre

class Post(models.Model):
    #Tupla de categorías de post
    OP_CATEGORIA = (
        ('S', 'Salud'),
        ('C', 'Servicio comunitario'),
        ('E', 'Educación'),
    )
    
    idpost = models.AutoField(primary_key=True)
    nombre_post = models.CharField(max_lenght = 300)
    iduser = models.ForeignKey('Usuario', on_delete = models.CASCADE)
    info = models.CharField(max_lenght = 2000)
    foto_post = models.FileField(upload_to=user_directory_path)
    fecha_post = models.DateField()
    #En la base de datos se guardará la opción como S, C o E
    Categoria = models.CharField(max_lenght = 2, choices = OP_CATEGORIA)

    def __unicode__(self):
        return self.nombre_post


class Sigue(models.Model):
    idsigue = models.AutoField(primary_key=True)
    iduser = models.ForeignKey('Usuario', on_delete = models.CASCADE)
    idpost = models.ForeignKey('Post', on_delete = models.CASCADE)
    
    def __unicode__(self):
        return self.idsigue


class Comentario(models.Model):
    idcomentario = models.AutoField(primary_key=True)
    iduser = models.ForeignKey('Usuario', on_delete = models.CASCADE)
    idpost = models.ForeignKey('Post', on_delete = models.CASCADE)
    texto = models.CharField(max_ñenght = 300)
    def __unicode__(self):
        return self.idcomentario