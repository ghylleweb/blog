from django import template

register = template.Library()

@register.inclusion_tag('posts/includes/blog_post.html', takes_context=True)
def post_detail(context, post):
    return {'post': post, 'context': context}