from django.shortcuts import render
from .models import Post, Comentario
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, ComentariosForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from taggit.models import Tag

"""class PostListView(ListView):
    queryset=Post.manage_perso.all()
    context_object_name='posts'
    paginate_by= 2
    template_name='blog/post/list.html'"""
    
def post_share(request, post_id):
    post = get_object_or_404(Post, pk=post_id, status=Post.Status.PUBLICO)
    sent=False
    if request.method == 'POST':
        form= EmailPostForm(request.POST)
        if form.is_valid():
            cd= form.cleaned_data
            post_url= request.build_absolute_uri(post.get_absolute_url())
            subject= f"{cd['nombre']} recommends you read {post.titulo}"
            message= f"Read {post.titulo} at {post_url}/n/n" \
                f"{cd['nombre']} \'s comentarios: {cd['comentarios']}"
            send_mail(subject,message,'nachozanetti0@gmail.com',[cd['to']])
            sent = True
    else:
        form= EmailPostForm()
    return render(request, 'blog/post/share.html',{'post':post, 'form':form, 'sent':sent})

def post_list (request, tag_slug= None):
    #usa el manage personalisado para obtener los post 
    posts_list = Post.manage_perso.all()
    tag = None
    if tag_slug:
        tag= get_object_or_404(Tag, slug=tag_slug)
        posts_list= posts_list.filter(tags__in=[tag])
    paginator = Paginator(posts_list,2)
    page_number= request.GET.get('page',1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts= paginator.page(1) 
    return render(request,'blog/post/list.html', {'posts': posts, 'tag':tag})

def post_detail (request,id, year, month, day, post):
    post = get_object_or_404(Post,
                             id = id,
                             slug=post,
                             status=Post.Status.PUBLICO,    
                             publicacion__year=year, 
                             publicacion__month=month, 
                             publicacion__day=day)
    comentarios= post.comentarios.filter(activo=True)
    form= ComentariosForm()
    return render(request,'blog/post/detail.html', {'post':post, 'comentarios':comentarios, 'form':form})

@require_POST
def post_comentario(request, post_id):
    post= get_object_or_404(Post, id=post_id, status=Post.Status.PUBLICO)
    comentario= None
    form= ComentariosForm(data=request.POST)
    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.post = post
        comentario.save()
    return render(request, 'blog/post/comentario.html', {'post':post, 'form':form, 'comentario':comentario}) 
 