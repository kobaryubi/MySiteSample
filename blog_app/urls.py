from django.urls import path
from . import views
from .views import *

app_name = 'blog_app'

urlpatterns = [
    path('', BlogsListView.as_view(), name='blogs_list'),
    path('create_blog', CreateBlogView.as_view(), name='create_blog'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('update_blog/<int:pk>', UpdateBlogView.as_view(), name='update_blog'),
    path('confirm_delete_blog/<int:pk>', ConfirmDeleteBlogView.as_view(), name='confirm_delete_blog'),
]