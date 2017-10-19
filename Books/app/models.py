# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    introduction = models.TextField()
    image = models.FileField(null=True)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title

class Article(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.name

#class Schedule(models.Model):
