from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import BlogPost


class BlogPostList(ListView):
    model = BlogPost
    paginate_by = 10
    context_object_name = "posts"

    def get_queryset(self):
        return self.model.objects.all().order_by('-date_created')


class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"