# admin.py
from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('taskname','description','date','priority','status')  # Remove 'fullname' and 'password1'


# Register the customized User admin
admin.site.register(Task, TaskAdmin)
