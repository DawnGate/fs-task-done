from django.shortcuts import HttpResponse, render

# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SignUpEmail
from .serializers import SignUpEmailSerializer

def index(request):
    return HttpResponse("Hello, World!")

class getAllSignUpEmail(APIView):
    
    def get(self, request):
        signUpEmails = SignUpEmail.objects.all()
        serializer = SignUpEmailSerializer(signUpEmails, many= True)
        return Response(serializer.data)


class addEmail(APIView):
    
    def post(self, request):
        data = {
            'email': request.data.get('email')
        }
        serializer = SignUpEmailSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)