from django.contrib import admin
from django.urls import path

from blog.views import BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path("admin/", admin.site.urls),
]
