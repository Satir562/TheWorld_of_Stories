from django.shortcuts import render

def index(request):
    return render(request, 'my_blog/index.html', {'title': 'главная страница'})

def about(request):
    return render(request,'my_blog/about.html', {'title': 'страница о нас'})
