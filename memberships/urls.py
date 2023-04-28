from django.urls import path
from memberships import views

app_name = "memberships"

urlpatterns = [
    path('membership-list', views.MembershipListView.as_view(), name="membership-list"),
]
