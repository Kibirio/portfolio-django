from django.urls import path
from .import views
from .views import index, create

urlpatterns = [
    path('', index, name='index'),
    path('create', create, name='create'),
]
