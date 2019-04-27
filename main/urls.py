from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_todo, name='add'),
    path('delete/<todo_id>', views.delete_todo, name='delete'),
    path('delete_all', views.delete_all, name='delete_all')
]
