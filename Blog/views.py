from django.shortcuts import render
from django.http import HttpResponse
from Blog.models import Blog, Author

# super username : Krishna
# password : ojha

def homePage(request):
    return render(request, 'home.html', {})

def blogPage(request):
    # list of the item of the blog database
    query = Blog.objects.all()
    context = {
        'items':query
    }
    print('hello this is query', query)
    return render(request, 'bloglist.html', context)
