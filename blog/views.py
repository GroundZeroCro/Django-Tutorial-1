# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

posts = [
    {
        'author': 'Zero',
        'title': 'Devv',
        'content': 'Android code',
        'date_posted': 'August 27, 2020.'
    },
    {
        'author': 'Ground',
        'title': 'Dev',
        'content': 'Angular code',
        'date_posted': 'August 21, 2020.'
    },
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)
