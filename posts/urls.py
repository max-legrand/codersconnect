from django.urls import path
from . import views
# Create your models here.
app_name = 'posts'
urlpatterns = [
    path('create_post/', views.create_post, name="create_post"),
    path('manage_post/', views.manage_posts, name="manage_post"),
    path('delete_post/', views.delete_post, name="delete_post"),
    path('edit_post/num=<int:num>', views.edit_post, name="edit_post"),
    path('view_listings/', views.view_listings, name="view_listings"),
    path('view_post/num=<int:num>', views.view_post, name="view_post"),
    path('filter_list', views.filter_list, name="filter_list")
]
