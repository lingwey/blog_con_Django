from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list (request):
    #posts = Post.objects.all()
    posts_list = Post.manage_perso.all()
    paginator = Paginator(posts_list,2)
    pege_number= request.GET.get('page',1)
    try:
        posts = paginator.page(pege_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts= paginator.page(1) 
    return render(request,'blog/post/list.html', {'posts': posts})

def post_detail (request,id, year, month, day, post):
    post = get_object_or_404(Post,
                             id = id,
                             slug=post,
                             status=Post.Status.PUBLICO,    
                             publicacion__year=year, 
                             publicacion__month=month, 
                             publicacion__day=day)
    return render(request,'blog/post/detail.html', {'post':post})
