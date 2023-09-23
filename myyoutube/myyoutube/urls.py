
from django.contrib import admin
from django.urls import path
from youtube import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('upload',views.upload,name='upload'),
    path('video/<int:pk>',views.video_detail,name='video_detail'),
    path('comment',views.comment,name='comment'),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]