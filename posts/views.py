from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from rest_framework import generics, permissions, viewsets, mixins, status

from rest_framework.response import Response

from rest_framework.views import APIView

from rest_framework.decorators import api_view


from django.db.models import Q

from django.contrib.auth import get_user_model

from .models import Post, CustomUser, PostLikes, PostDislikes

from django.http import JsonResponse

from .serializers import  PostSerializer,CustomUserDetailsSerializer, \
CustomRegisterSerializer, UserSerializer, PostLikeSerializer, PostDislikeSerializer

from .permissions import IsAuthorOrReadOnly



# Create your views here.


class PostList(generics.ListCreateAPIView):

    
    queryset = Post.objects.all()
    serializer_class= PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class UserList(generics.ListCreateAPIView):

    
    queryset = get_user_model().objects.all()
    serializer_class= UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    
    queryset = get_user_model().objects.all()
    serializer_class= UserSerializer






#Using function based views for likes and dislikes
#Checking of user already liked or disliked the post, if it did
#then remove users like or dislike, else like or dislike
@api_view(['GET', 'POST'])
def post_like_view(request, pk):
  

    post = Post.objects.get(pk=pk) 

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'POST':
        user=CustomUser.objects.get(username=request.user)
        try:
            PostLikes.objects.get(user=user, post_like=post).delete()
        except PostLikes.DoesNotExist:
            PostDislikes.objects.create(user=user, post_dislike=post)

        serializer = PostSerializer(post)
        return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def post_dislike_view(request, pk):
  

    post = Post.objects.get(pk=pk) 

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'POST':
        user=CustomUser.objects.get(username=request.user)
        try:
            PostDislikes.objects.get(user=user,post_dislike=post).delete()
        except PostDislikes.DoesNotExist:

            PostDislikes.objects.create(user=user, post_dislike=post)
        
        serializer = PostSerializer(post)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    































       





   