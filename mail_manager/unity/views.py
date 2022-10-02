from datetime import datetime, date
import django
from django.shortcuts import HttpResponse, render
from django import utils

# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SignUpEmail
from .serializers import SignUpEmailSerializer

def index(request):
    currentMonth = date.today().strftime("%B %Y")
    emailListCount = SignUpEmail.objects.count()
    newThisMonth = SignUpEmail.objects.filter(add_date__month = utils.timezone.now().month).count()
    unsubscriber = SignUpEmail.objects.filter(subcriber__exact=False).count()
    listEmails = SignUpEmail.objects.all()
    context = {
        'currentMonth': currentMonth,
        'emailListCount': emailListCount,
        'newThisMonth': newThisMonth,
        'unsubscriber': unsubscriber,
        'listEmails': listEmails
    }
    return render(request, 'unity/listEmailView.html', context)

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