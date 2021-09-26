from django.urls import path

from .views import home, form, create, view, edit, update, delete

urlpatterns = [
    #path('', views.index, name='index'),
    path('',home, name='home'),
    path('form/',form, name='form'),
    path('create/',create, name='create'),
    path('view/<int:pk>/',view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
]