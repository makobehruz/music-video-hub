from django.urls import path
from . import views


app_name = 'tracks'


urlpatterns = [
    path('list/', views.track_list, name='list'),
    path('form/', views.track_form, name='form'),
    path('video_list/', views.track_video, name='video_list'),
    path('detail/<int:pk>/', views.track_detail, name='detail'),
    path('delete/<int:pk>/', views.track_delete, name='delete'),
    path('update/<int:pk>/', views.track_update, name='update'),
]