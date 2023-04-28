from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import StudentTestimonials, DirectorMessage, TeamMembers, HomePageFAQ, BookDemoPage, CareerPage, ContactUsPage
# Register your models here.

admin.site.register(StudentTestimonials)
admin.site.register(DirectorMessage)
admin.site.register(TeamMembers)
admin.site.register(HomePageFAQ)
admin.site.register(BookDemoPage)
admin.site.register(CareerPage)
admin.site.register(ContactUsPage)