from django.contrib import admin

from job.models import Apply, Category, Job

#table display

class ApplyAdmin(admin.ModelAdmin):
    list_display = ('name','email','website','cv','created_at')




# Register your models here.
admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Apply,ApplyAdmin)