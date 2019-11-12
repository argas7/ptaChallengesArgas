# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-11 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='T\xedtulo')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cria\xe7\xe3o')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
            },
        ),
    ]