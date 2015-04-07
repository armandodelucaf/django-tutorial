# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dcc_colab', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name': 'T\xf3pico', 'verbose_name_plural': 'T\xf3picos'},
        ),
        migrations.AlterField(
            model_name='course',
            name='professors',
            field=models.ManyToManyField(to='dcc_colab.User', verbose_name='Professores', blank=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='course',
            field=models.ForeignKey(verbose_name='Disciplina', to='dcc_colab.Course'),
        ),
    ]
