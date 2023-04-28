from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db import models

from crm.models import JobCategory, JobDetail, JoinUs, ContactUs, ContactLeadFollowUp

# Register your models here.
admin.site.register(JobCategory)
admin.site.register(JobDetail)

admin.site.register(JoinUs)

admin.site.register(ContactUs)

@admin.register(ContactLeadFollowUp)
class ContactLeadFollowUpAdmin(admin.ModelAdmin):
    list_display = ['contact', 'owner', 'date', 'time', 'note', 'next_followup_date', 'next_followup_time']
