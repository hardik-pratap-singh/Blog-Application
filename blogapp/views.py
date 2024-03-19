from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
# def home(request):
#     return HttpResponse("<h1>Hello World</h1>")


posts = [
    {
        'author' : 'hps' , 
        'title' : 'abc' , 
        'content' : 'lorem34',
        'date_posted' : 'August 27, 2018'
    },
    {
        'author' : 'hpssingh' , 
        'title' : 'def' , 
        'content' : 'lorem2394',
        'date_posted' : 'August 15, 2018'
    },
    {
        'author' : 'hps12345' , 
        'title' : 'abcdefg' , 
        'content' : 'bengal tiger reserver',
        'date_posted' : 'August 27, 2020'
    }
]


def home(request):
    context = {
        'posts' : posts 
    }
    return render(request , 'blog/home.html' , context)


def about(request):
    return render(request , 'blog/about.html')
