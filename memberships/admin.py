from django.contrib import admin
from memberships.models import *
# Register your models here.


admin.site.register(MembershipType)
admin.site.register(Membership)
admin.site.register(UserMembership)

