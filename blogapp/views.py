from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse


# Create your views here.
# def home(request):
#     return HttpResponse("<h1>Hello World</h1>")


# posts = [
#     {
#         'author' : 'Sierra Elman' , 
#         'title' : 'The Future of Poetry' , 
#         'content' : 'Is AI Smarter Than an 8th Grader?',
#         'date_posted' : 'Mar 12, 2024'
#     },
#     {
#         'author' : 'Tim Berners-Lee' , 
#         'title' : 'Marking the Web’s 35th Birthday: An Open Letter' , 
#         'content' : 'Sir Tim Berners-Lee’s open letter to mark the occasion of the Web’s 35th Birthday.',
#         'date_posted' : 'Mar 11, 2024'
#     },
#     {
#         'author' : 'hps12345' , 
#         'title' : 'Would Albert Einstein End Up in Academia in 2024?' , 
#         'content' : 'Imagine that you are a young Albert Einstein in Gen Z, born 120 years after the legendary scientist, with a new concept for..',
#         'date_posted' : 'Mar 6, 2024'
#     }
# ]


def home(request):
    context = {
        'posts' : Post.objects.all() 
    }
    return render(request , 'blog/home.html' , context)


def about(request):
    return render(request , 'blog/about.html')
