from django.shortcuts import render,get_object_or_404
from a_blog.models import Post,Category
from a_webinfo.models import WebInfo

# Create your views here.
def home_view(request):
    webinfo_obj = WebInfo.objects.first()
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {'webinfo_obj': webinfo_obj, 'posts':posts, 'categories':categories}  # Add other blog data
    return render(request,'index.html',context)

def blog_post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog_post_detail.html', {'post': post})

def all_blogs(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'blogs.html',{'posts': posts, 'categories':categories})

def project_details(request):
    return render(request, 'projects.html')


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)  # Fetch the category by slug
    posts = Post.objects.filter(category=category, status='published')  # Filter published posts

    context = {'category': category, 'posts': posts}
    return render(request, 'category/category_detail.html', context)