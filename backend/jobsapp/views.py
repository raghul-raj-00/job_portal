from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Job, Application
from .serializers import JobSerializer, RegisterSerializer, ApplicationSerializer
from rest_framework import status
from django.contrib.auth.models import User
@api_view(['GET'])
def checking(request):
    return Response({"message": "Welcome to the Job Portal API!"})
@api_view(['POST'])
def userregister(request):
    serializer=RegisterSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response({"message": "User registered successfully!"},status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def login(request):
    username=request.data.get('username')
    password=request.data.get('password')
    try:
        user=User.objects.get(username=username,password=password)
        return Response({"user_id":user.id,"username":user.username,"message": "Login successful!"}, status=status.HTTP_200_OK)  
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
def joblist(request):
    jobs=Job.objects.all()
    serializer=JobSerializer(jobs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['POST'])
def applyjob(request):
    serializer=ApplicationSerializer(data=request.data)
    job_id=request.data.get('job')
    applicant= User.objects.first() 
    if(Application.objects.filter(job_id=job_id, applicant=applicant).exists()):
        return Response({"message": "already applied"}, status=status.HTTP_400_BAD_REQUEST)
    if(serializer.is_valid()):
        serializer.save(applicant=applicant)
        return Response({"message": "Applied successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
