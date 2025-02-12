from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('admin/', views.admin_view, name='admin'),
    path('user/', views.user_view, name='user'),
    path('curso/', views.curso_view, name='curso1'),
    path('curso2/', views.curso_view, name='curso2'),
    path('curso3/', views.curso_view, name='curso3'),
    path('curso4/', views.curso_view, name='curso4'),
    path('curso5/', views.curso_view, name='curso5'),
]