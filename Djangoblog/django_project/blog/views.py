from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS', 
        'title': 'Blog post 1', 
        'content': 'First post content', 
        'date_posted':'Auger 27, 2018'
    },
    {
        'author': 'Jane Doe', 
        'title': 'Blog post 2', 
        'content': 'Second post content', 
        'date_posted':'Auger 29, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html', context)


def about(request):
    return render(request,'blog/about.html',{'title':'About'})