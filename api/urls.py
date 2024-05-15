from django.contrib import admin
from django.urls import path,re_path 
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from a_blog.views import *
# from a_webinfo.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about_view, name='about'),
    path('blog/', all_blogs, name='blog'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('projects/', project_details, name='projects'),
    path('search/', search_posts, name='search_posts'),
    path('blog/<slug:slug>/', blog_post_detail, name='blog_post_detail'),
    path('',home_view)
]


# Use re_path for regular expression-based URL patterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Define media and static URL patterns using re_path
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]