from django.contrib import admin
from .models import Doctor
from .models import Ambulance
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Ambulance)