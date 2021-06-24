import posts
from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
# Create your views here.


#def index(request):
   # return HttpResponse('This is sample API')

def posts_list(request):
    posts=Post.objects.all()
    return render(request, template_name='list_of_posts.html', context={'posts': posts, 'is_retrieve': False})

def posts_retrieve(request, pk):
    posts=Post.objects.filter(id=pk)
    return render(request, template_name='list_of_posts.html', context={'posts': posts, 'is_retrieve': True })  

def create(request):
   return render(request, template_name='create_post.html')  

def create_post(request):
   data=request.POST
   posts=Post.objects.create(post_name=data['post name'], post_data=data['post data'])
   return render(request, template_name='list_of_posts.html', context={'posts': posts, 'is_retrieve': True })  


