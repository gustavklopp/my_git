from django.shortcuts import render
from weblog.models import Post, Tags
from django.views.generic import ListView, DetailView

def PostList(request):
    tags_list = Tags.objects.all()
    post_list = Post.objects.all()
    return render(request, 'weblog/post_list.html', {'post_list':post_list, 'tags_list':tags_list})

class PostDetailView(DetailView):
    model = Post


