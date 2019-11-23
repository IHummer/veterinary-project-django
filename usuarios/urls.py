from django.urls import path
from . import views

app_name = 'usuarios'
urlpatterns = [
    path('', views.index, name='index'),
    path('nuevo_usuario/', views.nuevo_usr, name='nuevo_usr'),
    path('<int:item_id>/', views.perfil_usr, name='perfil_usr')
]