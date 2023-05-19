from django.urls import path
from .views import posts_list, posts_details, posts_add, toggle_published

app_name='posts'

urlpatterns = [
    path('', posts_list, name='list'),
    path('<int:post_id>', posts_details, name='details'),
    path('toggle_published/<int:post_id>', toggle_published, name='toggle_published'),
    path('add', posts_add, name='add'),
]
