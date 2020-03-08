from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    #explicit one to invoke the models
    context_object_name = 'all_posts_list'