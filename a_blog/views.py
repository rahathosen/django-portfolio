from django.shortcuts import render,get_object_or_404
from a_blog.models import Post,Category
from django.db.models import Q
from a_webinfo.models import WebInfo

# Create your views here.
def home_view(request):
    title = WebInfo.objects.first().name
    webinfo_obj = WebInfo.objects.first()
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {'title': title, 'webinfo_obj': webinfo_obj, 'posts':posts, 'categories':categories}  # Add other blog data
    return render(request,'base.html',context)

def blog_post_detail(request, slug):
    webinfo_obj = WebInfo.objects.first()  
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog_post_detail.html', {'post': post, 'title': post.title, 'webinfo_obj':webinfo_obj})

def all_blogs(request):
    title = "Blog"
    posts = Post.objects.all()
    webinfo_obj = WebInfo.objects.first()
    categories = Category.objects.all()
    return render(request, 'blogs.html',{'posts': posts, 'webinfo_obj':webinfo_obj,'categories':categories, 'title': title})

def project_details(request):
    title = "Project"
    webinfo_obj = WebInfo.objects.first()
    return render(request, 'projects.html',{'title': title,'webinfo_obj':webinfo_obj})

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)  # Fetch the category by slug
    categories = Category.objects.all()
    webinfo_obj = WebInfo.objects.first()
    posts = Post.objects.filter(category=category, status='published', )  # Filter published posts
    title=category.name

    context = {'category': category, 'posts': posts, 'categories':categories, 'title':title, 'webinfo_obj':webinfo_obj}
    return render(request, 'category/category_detail.html', context)

def search_posts(request):
    webinfo_obj = WebInfo.objects.first()
 
    query = request.GET.get('query', '')  # Set default empty string for query
    if query:
        try:
            posts = Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            ).order_by('-created_at')
            categories = Category.objects.filter(posts__in=posts).distinct()
        except Exception as e:  # Catch any unexpected errors during database access
            
            
            context = {'error': f"An error occurred: {str(e)}", 'query': query}
            return render(request, 'search.html', context)

    else:
        posts = None  # No search query, display empty results or default message
        categories = []  # Empty categories list for consistency

    context = {'posts': posts, 'query': query, 'categories': categories,'title':query,'webinfo_obj':webinfo_obj}
    return render(request, 'search.html', context)



def header_view(request):
    webinfo_obj = WebInfo.objects.first() 

    context = {
        ' webinfo_obj': webinfo_obj,
    }

    return render(request, 'header.html', context)

def footer_view(request):
    webinfo_obj = WebInfo.objects.first() 

    context = {
        ' webinfo_obj': webinfo_obj,
    }
    return render(request, 'footer.html', context)


def about_view(request):
    title = "About"
    webinfo_obj = WebInfo.objects.first()
    # print( webinfo_obj.name)
    return render(request, 'about.html',{'title': title,'webinfo_obj':webinfo_obj})
