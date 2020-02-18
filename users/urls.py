from django.urls import path
from . import views
# Create your models here.
app_name = 'users'
urlpatterns = [
    path('login_user/', views.login_user, name="login_user"),
    path('signup_user/', views.signup_user, name="signup_user"),
    path('login_org/', views.login_org, name="login_org"),
    path('signup_org/', views.signup_org, name="signup_org"),
    path('logout/', views.logout_user, name="logout_user"),
]
