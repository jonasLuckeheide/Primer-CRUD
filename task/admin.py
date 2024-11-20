from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_de_creacion", ) 




admin.site.register(Task, TaskAdmin)


