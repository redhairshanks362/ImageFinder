from django.urls import path
from .views import AWSImageProcessing

urlpatterns = [
    path('getImage/', AWSImageProcessing.as_view()),
]