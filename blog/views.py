from django.shortcuts import render
# this will import the database class
from .models import Post
from django.views import generic


# Create your views here.
# DetailView is for a template that get its data from a model(database)
class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'


# TemplateView is for a template that do not get its data from a database.
class AboutView(generic.TemplateView):
    template_name = 'about.html'


# PostList is referenced in index.html as post_list
# ListView will render multiple data rows from the database
class PostList(generic.ListView):
    # this will query the Post Table
    # '-date_created' will reverse the order
    queryset = Post.objects.filter(status=1).order_by('-date_created')
    template_name = 'index.html'
