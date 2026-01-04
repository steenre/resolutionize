from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='landing'),
    path('new/', views.new, name='new'),
    path('home/', views.home, name='home'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
