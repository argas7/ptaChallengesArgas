# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Livros

# Register your models here.

class LivrosAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating')

admin.site.register(Livros, LivrosAdmin)