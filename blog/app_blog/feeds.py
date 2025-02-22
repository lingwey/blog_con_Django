import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post

class LatestPostsFeed(Feed):
    title = 'mi blog'
    link = reverse_lazy('blog:post_list')
    description = 'nuevo blog.'
    
    def items(self):
        return Post.manage_perso.all()[:5]
    
    def item_title(self, item):
        return item.titulo
    
    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.cuerpo),30)
    
    def item_pubdate(self, item):
        return item.publicacion