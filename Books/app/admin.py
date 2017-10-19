# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Book
from models import Article
# Register your models here.
admin.site.register(Book) #Add Book Model into admin page
admin.site.register(Article)