from django.urls import path
from . import views

# post:create
app_name = 'post'

urlpatterns = [
    path('',views.list, name='list'),
    path('create/',views.create, name='create'),
]