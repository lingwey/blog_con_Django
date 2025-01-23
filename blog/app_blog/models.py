from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#Manager personalizado
class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status= Post.Status.PUBLICO)

class Post (models.Model):
    
    class Status (models.TextChoices):
        BORRADOR = 'df', 'borrador'
        PUBLICO = 'pb', 'publico'
        
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publicacion')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    cuerpo = models.TextField()
    publicacion = models.DateTimeField(default=timezone.now)
    creacion = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.BORRADOR)
    
    class Meta:
        ordering =['-publicacion']
        indexes = [models.Index(fields=['-publicacion'])]
    
    objects= models.Manager()
    manage_perso= PublishManager()
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[ 
                                                 self.id,
                                                 self.publicacion.year, 
                                                 self.publicacion.month, 
                                                 self.publicacion.day, 
                                                 self.slug
                                                 ])
    