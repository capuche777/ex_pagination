from django.views.generic import ListView
from .models import Post


class BlogListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog_list.html'
