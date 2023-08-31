from django.urls import path
from core.views import HomeView

urlpatterns = [
    path('feed/',HomeView.as_view(),name='home_feed')
]