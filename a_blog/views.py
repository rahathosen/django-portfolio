from django.shortcuts import render
# from blog.models import WebInfo  
from a_webinfo.models import WebInfo

# Create your views here.
def home_view(request):
    webinfo_obj = WebInfo.objects.first()
    context = {'webinfo_obj': webinfo_obj, 'other_blog_data': ...}  # Add other blog data
    return render(request,'index.html',context)