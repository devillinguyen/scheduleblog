# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Book
from app.models import Article
from app.forms import RegistationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate#, login
#from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Bắt sự kiện get url /home
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest) # ???
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
# Bắt sự kiện get url /contact
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )
# Bắt sự kiện get url /about
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
# Bắt sự kiện get url /book
#@csrf_exempt
def book(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    Data = {
        'Books': Book.objects.all(),
        'title':'ListBook',
        'message':'Your ListBook right here:',
        'year':datetime.now().year,
    }
    if request.user.is_authenticated: # Authentication in Web requests
        return render(
            request,
            'app/book.html',
            Data
        )
    else:
        return HttpResponseRedirect("/login")

# Bắt sự kiện url /book/id
def intro(request, book_id):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    Data = {
        'book': Book.objects.get(pk=book_id), # Truy vấn dựa trên id của book
        'articles': Article.objects.all().filter(book_id=book_id), # Truy vấn đối tượng chapter có khóa ngoại là id của book
        'title':'Introduction',
        'year':datetime.now().year,
    }
    if request.user.is_authenticated: # Authentication in Web requests
        return render(
            request,
            'app/intro.html',
            Data
        )
    else:
        return HttpResponseRedirect("/login")
#
def article(request, article_id):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    Data = {
        'article': Article.objects.get(pk=article_id),
        'title':'Article',
        'year':datetime.now().year,
    }
    return render(
        request,
        'app/article.html',
        Data
    )
#
def register(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = RegistationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username = form.cleaned_data['username'], email = form.cleaned_data['email'], password=form.cleaned_data['password'])
            return HttpResponseRedirect("/login")
        return render(
            request,
            'app/register.html',
            {
                'form':form,
                'title':'Register'
            }
        )
    form = RegistationForm()
    return render(
        request,
        'app/register.html',
        {
            'form':form,
            'title':'Register'
        }
    )