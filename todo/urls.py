from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskView.as_view() , name='home'),
    path('add', views.add, name='add'),
    path('update', views.update, name='update'),
]