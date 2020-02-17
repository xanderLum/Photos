from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('api/upload/', views.PostPhotoView.as_view(), name='post_photo_view'),
    path('api/viewList/', views.ListPhotoView.as_view(), name='list_photo_view'),
]