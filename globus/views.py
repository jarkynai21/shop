from django.shortcuts import render
from django.db import models
from rest_framework import views, status
from rest_framework.response import Response
from .models import *
from .serializers import ProductSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated



class ProductAPIView(views.APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserView(views.APIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


    def get(self,request,*args,**kwargs):
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)
