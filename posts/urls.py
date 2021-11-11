from django.urls import path

from .views import PostList, PostDetail, UserList, UserDetail
from django.contrib.auth import views 

from . import views



from rest_framework.routers import DefaultRouter


urlpatterns = [

    #user list and user details
    path('users/<int:pk>',UserDetail.as_view()),
    path('users/',UserList.as_view()),
    
    #post list, post detail, 
    path('',PostList.as_view()),
    path('<int:pk>/',PostDetail.as_view()),
   
    
    #like/dilike posts
    path('like/<int:pk>',views.post_like_view,name = 'post_likes'),
    path('dislike/<int:pk>',views.post_dislike_view,name = 'post_likes'),

    






    
]

