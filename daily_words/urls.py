from django.urls import path

from . import views

urlpatterns = [
    path('api/save', views.save_word, name='save'),
    path('api/delete', views.delete_word, name='delete')
]