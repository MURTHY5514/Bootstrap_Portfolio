from django.contrib import admin
from Portfolio.models import Contact,Internship
# Register your models here.

class InternshipAdmin(admin.ModelAdmin):
    list_display=('fullname','usn','college_name','proj_report')
    search_fields=('fullname','usn')
    list_filter=['college_name','proj_report','offter_status']
admin.site.register(Contact)
admin.site.register(Internship,InternshipAdmin)
