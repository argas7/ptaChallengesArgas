# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Livros(models.Model):
    title = models.CharField('Título', max_length=50)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
    
    def __str__(self):
        return self.title