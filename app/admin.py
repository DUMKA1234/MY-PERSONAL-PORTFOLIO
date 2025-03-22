from django.contrib import admin
from .import models
admin.site.register(models.students)
admin.site.register(models.course)
admin.site.register(models.school)


# Register your models here.
