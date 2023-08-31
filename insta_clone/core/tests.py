from django.urls import path
from authentication.views import SignUpView , SignInView,home
urlpatterns =[
    # path('', home = name='home_view'),
    path('feed/',HomeView.as_view() ,name='home_feed'),
    path('signin/',SignInView.as_view() ,name='signin_view')
]