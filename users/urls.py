from django.urls import path, include
from django.contrib import admin
# from django.contrib.auth import views as auth_views
from users import views

app_name = 'users'

urlpatterns = [

    path('login/', views.signin, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name='home'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout-user'),

]

