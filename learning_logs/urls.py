"""Define padrões de URL para learning_logs."""
from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'learning_logs'
urlpatterns = [
    # Página inicial
    #url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),

    # Mostra todos os assuntos
    #url(r'^topics/$', views.topics, name='topics'),
    path('topics/', views.topics, name='topics'),

    # Página de detalhes para um único assunto
    # url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    path('topics/<int:topic_id>)/', views.topic, name='topic'),

    # Página para adicionar um novo assunto
    # url(r'^new_topic/$', views.new_topic, name='new_topic'),
    path('new_topic/', views.new_topic, name='new_topic'),

    # Página para adicionar uma nova entrada
    # url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    path('new_entry/<int:topic_id>)/', views.new_entry, name='new_entry'),

    # Página para editar uma entrada
    # url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    path('edit_entry/<int:entry_id>)/', views.edit_entry, name='edit_entry'),


]

