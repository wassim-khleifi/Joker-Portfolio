from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from pages.models import *
from .serializer import *
# Create your views here.
@api_view(['get'])
def projects(request):
	projects = Projects.objects.all()
	serializer = ProjectsSerializer(projects, many=True)
	return Response(serializer.data)

@api_view(['get'])
def jobs(request):
	jobs = Jobs.objects.all()
	serializer = JobsSerializer(jobs, many=True)
	return Response(serializer.data)
