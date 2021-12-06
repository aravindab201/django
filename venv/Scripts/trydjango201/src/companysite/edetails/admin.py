from django.contrib import admin
from .models import employee,dept

# Register your models here.
admin.site.register([employee,dept])
#admin.site.register(dept)

