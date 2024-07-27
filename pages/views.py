from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import json, requests
# Create your views here.
with open('portfolio.config.json', 'r') as fp:
	config = json.load(fp)
def index(request):
	projects = Projects.objects.all()
	jobs = Jobs.objects.all()
	ctx = {'config': config['Config'],'projects': projects if projects else None,"jobs": jobs if jobs else None}
	if request.method == "POST":
		email = request.POST.get('email')
		name = request.POST.get('name')
		message = request.POST.get('message')
		data = {
		"content" : f"**EMAIL**: {email}\n**NAME:** {name}\n**MESSAGE:** {message}"
		}
		result = requests.post(config['Config']["contact"]["webhook_url"], json=data)
	return render(request, 'pages/index.html',ctx)

def blog(request):
	return HttpResponse("Coming soon.")