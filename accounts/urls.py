from django.urls import path
from accounts.views import signup
from accounts.views import user_login
from accounts.views import user_logout


urlpatterns = [
    path("signup/", signup, name='signup'),
    path("login/", user_login, name="user_login"),
    path("logout/", user_logout, name="user_logout"),
]
