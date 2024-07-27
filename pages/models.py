from django.db import models
from django.core.exceptions import ValidationError

def validate_only_one_instance(obj):
	model = obj.__class__
	if (model.objects.count() > 0 and
			obj.id != model.objects.get().id):
		raise ValidationError("ERROR: You can only create 1 config instance.")

# Create your models here.
class Projects(models.Model):
	banner = models.ImageField(upload_to='pages/photos',verbose_name='Project banner')
	name = models.CharField(max_length=50000,verbose_name="Project name")
	description = models.TextField(max_length=500, verbose_name="Project description")
	redirect = models.CharField(max_length=50000,verbose_name="Project url")
	def __str__(self):
		return self.name

class Jobs(models.Model):
	name = models.CharField(max_length=100,verbose_name="Job name")
	description = models.CharField(max_length=200, verbose_name="Job rank")
	banner = models.ImageField(upload_to='pages/photos',verbose_name='Job banner')
	redirect = models.URLField(verbose_name='Job redirect link')
	def __str__(self):
		return self.name
