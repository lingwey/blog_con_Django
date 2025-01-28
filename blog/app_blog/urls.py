from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    #desde post views
    #path('',views.post_list, name='post_list'),
    path('',views.PostListView.as_view(), name='post_list'),
    path('<int:id>/<int:year>/<int:month>/<int:day>/<slug:post>',views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comentario/', views.post_comentario, name='post_comentario'),
]
