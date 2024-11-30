from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('pagprote/', views.pagprote, name='pagprote'),
    path('logout/', views.logout_view, name='logout'),
]
