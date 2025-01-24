from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm

class PostListView(ListView):
    queryset=Post.manage_perso.all()
    context_object_name='posts'
    paginate_by= 2
    template_name='blog/post/list.html'
    
def post_share(request, post_id):
    post = get_object_or_404(Post, pk=post_id, status=Post.Status.PUBLICO)
    if request.method == 'POST':
         form= EmailPostForm(request.POST)
    if form.is_valid():
        cd= form.cleaned_data
    else:
        form= EmailPostForm()
    return render(request, 'blog/post/sshare.html',{'post':post, 'form':form})
def post_list (request):
    #usa el manage personalisado para obtener los post 
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
