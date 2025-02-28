from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('administracion/', views.admin_view, name='administracion'),
    path('administracion/cambiar_estado_usuario/<int:usuario_id>/', views.cambiar_estado_usuario, name='cambiar_estado_usuario'),
    path('user/', views.user_view, name='user'),
    path('curso/', views.curso_view, name='curso1'),
    path('curso2/', views.curso2_view, name='curso2'),
    path('curso3/', views.curso3_view, name='curso3'),
    path('curso4/', views.curso4_view, name='curso4'),
    path('curso5/', views.curso5_view, name='curso5'),
    path('error/', views.error_view, name='error'),
]

#descomentar para ver los archivos en el administracion
# Añadir configuración para servir archivos media
if settings.DEBUG:
   
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)