from django.urls import path
from .views import post_list, post_details, add_post, edit_post, delete_post

urlpatterns = [
    path('', post_list, name='post-list'),
    path('<int:pid>/', post_details, name='post-details'),
    path('add/', add_post, name='new-post'),
    path('<int:pid>/edit/', edit_post, name='edit-post'),
    path('<int:pid>/delete/', delete_post, name='delete-post'),
]
