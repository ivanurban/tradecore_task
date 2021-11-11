from django.db import models

from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser


# Create your models here.

#CustomUser class serves as user profile, inherited from class AbstractUser
# added fields for location a nd registration_local_holiday
class CustomUser(AbstractUser):
    
    location = models.CharField(max_length=200,null=True, blank=True ) 
    registration_local_holiday = models.CharField(max_length=200,null=True, blank=True)


#user can have many posts
class Post(models.Model):
    
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.post_body

    def get_likes_count(self):
        return PostLikes.objects.filter(post_like=self).count()

    def get_dislikes_count(self):
        return PostDislikes.objects.filter(post_dislike=self).count()


class PostLikes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True ) 
    post_like = models.ForeignKey(Post, related_name='liked', on_delete=models.CASCADE, null=True )

    def __str__(self):
        return f'user:{self.user} liked {self.post_like}'

class PostDislikes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    post_dislike = models.ForeignKey(Post, related_name='Disliked', on_delete=models.CASCADE, null=True)

        






