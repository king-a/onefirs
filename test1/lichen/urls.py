from django.urls import path

from . import views

app_name = 'lichen'

urlpatterns = [
    path('',views.index,name='index'),
    path('lichen/',views.lichen,name='lichen'),
]

