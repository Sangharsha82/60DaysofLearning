from django.shortcuts import render
from django.http import HttpResponse

posts = [{    'author': 'John Doe',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'August 27, 2018'},
    
    {'author': 'John Doe',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'August 27, 2018'},
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html', context)

