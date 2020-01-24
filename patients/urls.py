from django.urls import path, include
from django.contrib import admin
# from django.contrib.auth import views as auth_views
from patients import views

app_name = 'patients'

urlpatterns = [

    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^admin/', admin.site.urls),


    path('appointments/', views.appointments, name='login'),
    # path('signup/', views.signup, name='signup'),
    # path('home/', views.home, name='home'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout-user'),

    # path('delete/<int:pk>', views.DeleteEvent.as_view(), name='event-delete'),
    # path('update/<int:pk>', views.UpdateEvent.as_view(), name='event-update'),
    # path('publish', views.PublishEvent.as_view(), name='publish-event'),

]

