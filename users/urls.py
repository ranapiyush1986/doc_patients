from django.urls import path, include
from django.contrib import admin
# from django.contrib.auth import views as auth_views
from users import views

app_name = 'users'

urlpatterns = [

    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^admin/', admin.site.urls),

    path('login/', views.signin, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name='home'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout-user'),

    # path('delete/<int:pk>', views.DeleteEvent.as_view(), name='event-delete'),
    # path('update/<int:pk>', views.UpdateEvent.as_view(), name='event-update'),
    # path('publish', views.PublishEvent.as_view(), name='publish-event'),

]

