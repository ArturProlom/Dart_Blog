from django import template
from blog.models import Post, Tag

register = template.Library()


@register.inclusion_tag('blog/popular_posts.html')
def get_popular_posts(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}


@register.inclusion_tag('blog/tags_tpl.html')
def get_tags(cnt=20):
    tags = Tag.objects.all()[:cnt]
    return {'tags': tags}

