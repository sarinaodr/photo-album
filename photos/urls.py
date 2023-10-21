from django.urls import path

from .views import gallery , photoview , categoryview , addphoto

urlpatterns = [
    path('' , gallery , name='gallery'),
    path('photo/<int:pk>/', photoview , name='photo'),
    path('category/<int:pk>/' , categoryview , name='category'),
    path('upload/' , addphoto , name='addphoto')
    
]
