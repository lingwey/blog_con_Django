from django.contrib import admin
from .models import Post, Comentario


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'slug','autor', 'publicacion', 'status']
    list_filter = ['status', 'creacion', 'publicacion', 'autor']
    search_fields = ['titulo','cuerpo']
    prepopulated_fields= {'slug': ('titulo',)}
    raw_id_fields = ['autor']
    date_hierarchy = 'publicacion'
    ordering= ['status', 'publicacion']
    
@admin.register(Comentario)
class ComentariosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'post', 'creacion', 'activo']
    list_filter= ['activo', 'creacion', 'actualizacion']
    search_fields = ['nombre', 'email', 'cuerpo' ]