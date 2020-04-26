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
    path('filter_list', views.filter_list, name="filter_list"),
    path('apply', views.apply, name="apply"),
    path('withdraw', views.withdraw, name="withdraw"),
    path('view_jobs', views.view_jobs, name="view_jobs"),
    path('status_update', views.statusChange, name="status_update"),
    path('view_applicants/num=<int:num>', views.view_applicants, name="view_applicants"),
    path('status_applicant', views.status_applicant, name="status_applicant"),
    path('view_jobs_accepted', views.view_jobs_accepted, name="view_jobs_accepted"),
    path('view_connections', views.view_connections, name="view_connections"),
    path('status_connection', views.status_connection, name="status_connection"),
    path('close_listing', views.close_listing, name="close_listing"),
    path('open_listing', views.open_listing, name="open_listing")
]
