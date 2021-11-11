from rest_framework import serializers

from allauth.account.adapter import get_adapter

from .models import Post, CustomUser, PostLikes,PostDislikes

from dj_rest_auth.registration.serializers import RegisterSerializer

from django.contrib.auth import get_user_model

#importing celery tasks 
from .tasks import get_location, get_local_holiday, user_location


#imported methods from tasks.py(using celery for async calls), calling the delay() method of the tasks to execute it asynchronously.
#The tasks will be added to the queue and will be executed by a worker as soon as possible.
get_location.delay()
user_location.delay()
get_local_holiday.delay()


class CustomRegisterSerializer(RegisterSerializer):

    location = serializers.CharField(max_length=200, default=user_location)
    registration_local_holiday = serializers.CharField(max_length=200, default=get_local_holiday)

    class Meta:
        model=CustomUser
        fields = ('id','username','email','password','location','registration_local_holiday', )


    # override get_cleaned_data of RegisterSerializer
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'location': self.validated_data.get('location'),
            'registration_local_holiday': self.validated_data.get('registration_local_holiday'),
          
        }

    # override save method of RegisterSerializer
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.location = self.cleaned_data.get('location')
        user.registration_local_holiday = self.cleaned_data.get('registration_local_holiday')
      
        user.save()
        adapter.save_user(request, user, self)
        return user


#Get user details
class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'email',
            'location',
            'registration_local_holiday',
        )
        read_only_fields = ('location',)



class PostLikeSerializer(serializers.ModelSerializer):


    class Meta:
        model = PostLikes
        fields = ( 'post_like',)


class PostDislikeSerializer(serializers.ModelSerializer):


    class Meta:
        model = PostDislikes
        fields = ( 'post_dislike',)


class PostSerializer(serializers.ModelSerializer):

    dislikes = serializers.IntegerField(source='get_dislikes_count',read_only=True)
    likes = serializers.IntegerField(source='get_likes_count',read_only=True)
    #liked = PostLikeSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('id','author', 'post_body','pub_date','likes', 'dislikes')





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= get_user_model()
        fields=('id','username','email','location','registration_local_holiday')


    













