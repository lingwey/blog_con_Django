from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    #desde post views
    path('',views.post_list, name='post_list'),
    path('<int:id>/',views.post_detail, name='post_detail'),
]
