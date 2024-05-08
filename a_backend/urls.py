from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from a_blog.views import *
from a_webinfo.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about_view, name='about'),
    path('blog/', all_blogs, name='blog'),
    path('projects/', project_details, name='projects'),
    path('blog/<slug:slug>/', blog_post_detail, name='blog_post_detail'),
    path('',home_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
