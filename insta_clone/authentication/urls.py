from django.urls import path
from authentication.views import SignUpView , SignInView, home, SignOutView
urlpatterns =[
    path('',home,name='home_view'),
    path('signup/',SignUpView.as_view() ,name='signup_view'),
    path('signin/',SignInView.as_view() ,name='signin_view'),
    path('signout/',SignOutView.as_view() ,name='signout_view'),

]