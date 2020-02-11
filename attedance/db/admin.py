from django.contrib import admin
from .models.library import Employee, Attendance

# Register your models here.
admin.site.register(Employee)
admin.site.register(Attendance)
