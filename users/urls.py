from django.urls import path
from .views import loginview , logoutview , registerview

app_name = "users"

urlpatterns = [
    path('login/' , loginview , name='login'),
    path('logout/' , logoutview , name='logout'),
    path('register/' , registerview , name='register'),
    
]
