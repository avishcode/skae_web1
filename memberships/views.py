from django.shortcuts import render
from memberships.models import *
from django.views.generic import ListView
# Create your views here.

def MembershipList(request):
    return render(request, "memberships/admin/membership_list.html")


class MembershipListView(ListView):
    model = Membership
    template_name = "memberships/admin/membership_list.html"


