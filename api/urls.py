from django.urls import path,include
from . import views
## add urls
urlpatterns = [
	path('projects', views.projects, name="projects_api"),
	path('jobs', views.jobs, name='jobs_api')
]