from rest_framework import routers
from django.urls import path
from .views import *

router = routers.DefaultRouter()

urlpatterns = [

    path('user/', UserView.as_view()),
    path('product/', ProductAPIView.as_view()),

]