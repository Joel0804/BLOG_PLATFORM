from django.urls import path
from .import views

urlpatterns = [
    path('login',views.login_user, name='login'), 
    path('register', views.register_user, name='register'),
    path('', views.home, name='home'),
    path('create',views.create_post, name='create_post'),
    path('update/<int:pk>', views.update_post, name='update_post'),
    path('delete/<int:pk>', views.delete_post, name='delete_post'),
    path('logout', views.logout_user, name='logout'),  
    path('post/<int:pk>', views.post_detail, name='post_detail'),
]
