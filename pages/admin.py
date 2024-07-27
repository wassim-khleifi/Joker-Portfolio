from django.contrib import admin
from .models import *
# Register your models here.
## Config
admin.site.site_title = 'Portfolio Administration'
admin.site.index_title = 'Dashboard'
admin.site.site_header = 'Portfolio Admin Panel'
## Models
admin.site.register(Projects)
admin.site.register(Jobs)
