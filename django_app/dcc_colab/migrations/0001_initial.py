# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.CharField(max_length=255, verbose_name='Avalia\xe7\xe3o')),
                ('year', models.CharField(max_length=4, verbose_name='Ano')),
                ('semester', models.SmallIntegerField(verbose_name='Per\xedodo')),
                ('course', models.ForeignKey(to='dcc_colab.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.CharField(max_length=255, verbose_name='Conte\xfado')),
                ('test', models.ForeignKey(to='dcc_colab.Test')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestContentRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.CharField(default=b'RATE', max_length=15, choices=[(b'RATE', b'Nota'), (b'REPORT', b'Den\xc3\xbancia')])),
                ('test_content', models.ForeignKey(to='dcc_colab.TestContent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.CharField(default=b'RATE', max_length=15, choices=[(b'RATE', b'Nota'), (b'REPORT', b'Den\xc3\xbancia')])),
                ('test', models.ForeignKey(to='dcc_colab.Test')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Tema')),
                ('course', models.ForeignKey(to='dcc_colab.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TopicContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.CharField(max_length=255, verbose_name='Conte\xfado')),
                ('topic', models.ForeignKey(to='dcc_colab.Topic')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TopicContentRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.CharField(default=b'RATE', max_length=15, choices=[(b'RATE', b'Nota'), (b'REPORT', b'Den\xc3\xbancia')])),
                ('topic_content', models.ForeignKey(to='dcc_colab.TopicContent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facebook_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Membro desde')),
                ('type', models.CharField(default=b'A', max_length=1, choices=[(b'P', b'Professor'), (b'A', b'Aluno')])),
            ],
            options={
                'ordering': ['creation_date'],
                'verbose_name': 'Usu\xe1rio',
                'verbose_name_plural': 'Usu\xe1rios',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='topiccontentrate',
            name='user',
            field=models.ForeignKey(to='dcc_colab.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='topiccontent',
            name='user',
            field=models.ForeignKey(to='dcc_colab.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testrate',
            name='user',
            field=models.ForeignKey(to='dcc_colab.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcontentrate',
            name='user',
            field=models.ForeignKey(to='dcc_colab.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcontent',
            name='user',
            field=models.ForeignKey(to='dcc_colab.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='test',
            name='professor',
            field=models.ForeignKey(related_name='professor', to='dcc_colab.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='test',
            name='topics',
            field=models.ManyToManyField(to='dcc_colab.Topic'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='test',
            name='user',
            field=models.ForeignKey(related_name='user', to='dcc_colab.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='professors',
            field=models.ManyToManyField(to='dcc_colab.User'),
            preserve_default=True,
        ),
    ]
