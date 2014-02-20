from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    list_display = ('title', 'date_created', 'date_last_edit', 'visible_until', 'url')

    def url(self, obj):
        return '<a href="%s">See on site</a>' % obj.get_absolute_url()
    url.allow_tags = True

admin.site.register(BlogPost, BlogPostAdmin)