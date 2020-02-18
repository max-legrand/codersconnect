from django.urls import path
from . import views
# Create your models here.
app_name = 'posts'
urlpatterns = [
    path('create_post/', views.create_post, name="create_post"),
]
