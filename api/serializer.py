from rest_framework import serializers
from pages.models import Projects, Jobs

## serializers here:
class ProjectsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Projects
		fields = '__all__'

class JobsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Jobs
		fields = '__all__'