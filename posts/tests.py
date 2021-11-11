from django.test import TestCase

from .models import Post,PostLikes,PostDislikes

#from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your tests here.

class PostTestCase(TestCase):
  
    #create a User
    def setUp(self):
        
        testuser1 = User.objects.create_user(username="testuser1", email="testuser100@test.com", password="test@123")
        testuser1.save()

        #create a post
        testpost = Post.objects.create(author=testuser1, post_body="A prime is a positive integer X that has exactly \
                                                                     two distinct divisors: 1 and X. The first few prime \
                                                                     integers are 2, 3, 5, 7, 11 and 13.")

        testpost.save()    

    
    def test_post_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        post_body = f'{post.post_body}'
        self.assertEqual(author,'testuser1')
        self.assertEqual(post_body,"A prime is a positive integer X that has exactly \
                                                                     two distinct divisors: 1 and X. The first few prime \
                                                                     integers are 2, 3, 5, 7, 11 and 13.")         


    def test_like_post(self):
        post = Post.objects.get(id=1)
        user=User.objects.get(username="testuser1")
        PostLikes.objects.create(user=user, post_like=post)
        self.assertEqual(PostLikes.objects.filter(post_like=post).count(),1)


    def test_dislike_post(self):
        post = Post.objects.get(id=1)
        user=User.objects.get(username="testuser1")
        PostDislikes.objects.create(user=user, post_dislike=post)
        self.assertEqual(PostDislikes.objects.filter(post_dislike=post).count(),1)


