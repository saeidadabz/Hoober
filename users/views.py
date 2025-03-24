from django.shortcuts import render

from .models import User
from .serializer import UserRegisterSerializer 


from rest_framework.views import APIView
from rest_framework.response import Response  
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from drf_spectacular.utils import extend_schema

class UserRegisterView(APIView):

    @extend_schema(
        request=UserRegisterSerializer,
        responses={201: UserRegisterSerializer},
    )
    def post(self,request):
        
        email=request.data.get('email')

        if User.objects.filter(email=email).exists():
            return Response({'detaail':'user alreaaady registered'})


        serializer=UserRegisterSerializer(data=request.data)

       


        if serializer.is_valid():
          
            user = User.objects.create_user(
                email=serializer.validated_data['email'],
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password'],
                role=serializer.validated_data['role'],

            )

            refresh=RefreshToken.for_user(user)
            access_token=refresh.access_token
            
            token={
                "refresh":str(refresh),
                "access_token":str(access_token)
            }
            user_serializer= UserRegisterSerializer(user,context={'token':token})
           
            return Response(user_serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



