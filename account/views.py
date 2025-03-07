from django.shortcuts import render
from rest_framework.decorators import api_view 
from .serializers import SignUPSerializer , UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework  import status
from django.contrib.auth.hashers import make_password
# Create your views here.





@api_view(['POST'])
def register(request):
    data = request.data
    user = SignUPSerializer(data= data)
    
    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists():  #  اتخقق انو مانو مسجل مسبقا 
            user = User.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'], 
                email  = data['email'], 
                username= data['email'],
                password = make_password(data['password'])
            )
            return Response({'details':'Your Account Registerd SeccessFully!'} , status= status.HTTP_201_CREATED)
        else:
            return Response({'error':'This email already exists!'} , status= status.HTTP_400_BAD_REQUEST)
    else:
        return Response(user.errors)






@api_view(['GET'])
def userInfo(request):
	user = UserSerializer(request.user , many=False)
	return Response(user.data) # Return Info User

	