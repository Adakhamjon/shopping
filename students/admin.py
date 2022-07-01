from django.contrib import admin

from .models import *
admin.site.register(Faculty),
admin.site.register(Course),
admin.site.register(Stage),
admin.site.register(Group),
admin.site.register(Student)
