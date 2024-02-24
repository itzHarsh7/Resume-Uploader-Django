from django.contrib import admin

# Register your models here.
from .models import Resume

class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','dob','city','state']
admin.site.register(Resume, ResumeAdmin)