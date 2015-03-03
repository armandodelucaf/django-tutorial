# -*- encoding: utf-8 -*-

from datetime import datetime
from django.db import models

class User(models.Model):
    PROFESSOR = 'P'
    STUDENT = 'A'
    USER_TYPES = (
        (PROFESSOR, 'Professor'),
        (STUDENT, 'Aluno')
    )
    facebook_id = models.CharField(max_length=20)
    name = models.CharField(max_length=200, verbose_name=u'Nome')
    creation_date = models.DateTimeField(default=datetime.now, verbose_name=u'Membro desde')
    type = models.CharField(max_length=1, choices=USER_TYPES, default=STUDENT)

    class Meta:
        ordering = ["creation_date"]
        verbose_name = u'Usuário'
        verbose_name_plural = u'Usuários'

    def __str__(self):
        return self.name.encode('utf-8')

class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Nome')
    professors = models.ManyToManyField(User)

    class Meta:
        verbose_name = u'Disciplina'
        verbose_name_plural = u'Disciplinas'

    def __str__(self):
        return self.name.encode('utf-8')

class Topic(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Tema')
    course = models.ForeignKey(Course)

    def __str__(self):
        return self.name.encode('utf-8')

class Test(models.Model):
    source = models.CharField(max_length=255, verbose_name=u'Avaliação')
    year = models.CharField(max_length=4, verbose_name=u'Ano')
    semester = models.SmallIntegerField(verbose_name=u'Período')
    user = models.ForeignKey(User, related_name="user")
    course = models.ForeignKey(Course)
    professor = models.ForeignKey(User, related_name="professor")
    topics = models.ManyToManyField(Topic)

class TestContent(models.Model):
    test = models.ForeignKey(Test)
    source = models.CharField(max_length=255, verbose_name=u'Conteúdo')
    user = models.ForeignKey(User)

class TopicContent(models.Model):
    topic = models.ForeignKey(Topic)
    user = models.ForeignKey(User)
    source = models.CharField(max_length=255, verbose_name=u'Conteúdo')

class TestRate(models.Model):
    RATE = 'RATE'
    REPORT = 'REPORT'
    TYPES = (
        (RATE, 'Nota'),
        (REPORT, 'Denúncia')
    )
    user = models.ForeignKey(User)
    test = models.ForeignKey(Test)
    grade = models.CharField(max_length=15, choices=TYPES, default=RATE)

class TestContentRate(models.Model):
    RATE = 'RATE'
    REPORT = 'REPORT'
    TYPES = (
        (RATE, 'Nota'),
        (REPORT, 'Denúncia')
    )
    user = models.ForeignKey(User)
    test_content = models.ForeignKey(TestContent)
    grade = models.CharField(max_length=15, choices=TYPES, default=RATE)

class TopicContentRate(models.Model):
    RATE = 'RATE'
    REPORT = 'REPORT'
    TYPES = (
        (RATE, 'Nota'),
        (REPORT, 'Denúncia')
    )
    user = models.ForeignKey(User)
    topic_content = models.ForeignKey(TopicContent)
    grade = models.CharField(max_length=15, choices=TYPES, default=RATE)
