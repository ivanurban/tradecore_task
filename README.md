# tradecore_task
###This a django rest application, that enables user to:
  - Register, Login
  - Create, Update, Delete Posts
  - Like or dislike posts(only one like or dislike per post). Trying to like or dislike poste twice results in removing like or dislike
  
 
###Application uses dj-rest-auth third party application for authentication

    Endpoints:

    - api/v1/dj-rest-auth/login/

    - api/v1/dj-rest-auth/logout/

    - api/v1/dj-rest-auth/password/reset/

    - api/v1/dj-rest-auth/password/reset/confirm

    For user registration additional third part app in nedded, django-allauth,

    Endpoint:

    - api/v1/dj-rest-auth/registration/

   This is how settings.py should look:
     #third-party apps
      'rest_framework',
      'rest_framework.authtoken', #generates the tokens on the server
      'allauth',
      'allauth.account',
      'allauth.socialaccount', #if using social-network accounts
      'dj_rest_auth', #log in log out, password reset API endpoints
      'dj_rest_auth.registration'

###List of all posts, Adding a  new post:
  - Endpoint:
    - api/v1/

###Post Update/delete:
  - Endpoint:
    - api/v1/{id ofa post}
    
###Liking/Disliking posts
  - Endpoints:
    - api/v1/like{id of a post}
    - api/v1/dislike{id of a post}
    
###When user is registered, Abstract API (https://www.abstractapi.com/)is used o find the location of user by IP,
    and to check if there is a national holiday on the day of the user registration, these information are saved 
    in a database in CustomUser.

    For communication with Abstract API, third party app Celery is used. Celery is a distributed task queue that can process vast amounts of messages. Using
    Celery, not only can you create asynchronous tasks easily and let them be executed by workers as soon as possible. 
    In addition Celery is set to use automatically retrying failed celery tasks,in this app exponential backoff is used to avoid overwhelming the service.

    Celery also needs message broker, I used RabbitMQ, but Redis is fine also.
    
###There are a few testsin posts/tests.py file
   


  











 


 
  
