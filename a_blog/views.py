from django.shortcuts import render,get_object_or_404
from a_blog.models import Post
from a_webinfo.models import WebInfo

# Create your views here.
def home_view(request):
    webinfo_obj = WebInfo.objects.first()
    posts = Post.objects.all()
    context = {'webinfo_obj': webinfo_obj, 'posts':posts}  # Add other blog data
    return render(request,'index.html',context)

def blog_post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog_post_detail.html', {'post': post})