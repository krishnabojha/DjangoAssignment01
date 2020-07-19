from django.contrib import admin
from django.urls import path
from Blog.views import homePage, blogPage

urlpatterns = [
    path('',homePage),
    path('home/', homePage),
    path('blog/', blogPage)
]