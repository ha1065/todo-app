from django.conf.urls import url
from django.urls import path
from django.utils import timezone

from .views import index, TaskCreateView, TaskDetailView, TaskDeleteView, TaskUpdateView

app_name = 'tasks'
urlpatterns = [
    path('', index, name='index'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='update'),
    path('<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete'),

]