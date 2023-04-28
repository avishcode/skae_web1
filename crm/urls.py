from django.urls import path

from crm import adminViews
from crm import counsellorViews


from crm.views import *

app_name = "crm"

urlpatterns = [

    # Admin Views 
    path('contact-list', adminViews.ContactUsList.as_view(), name='contact-list'), 
    path('contact-list/<pk>/', adminViews.ContactUsDetailView.as_view(), name='contact-detail'),
    path('update/<pk>', adminViews.ContactUsUpdateView.as_view(), name='update-contact'),
    path('job-application-list', adminViews.JobApplicationList.as_view(), name='job-application-list'),
    path('contact-followup', adminViews.ContactLeadFollowUpCreateView.as_view(), name='contact-followup'), 
    path('demo-st-list', adminViews.BookDemoListView.as_view(), name="demo-st-list"),

    # Counsellor Views
    path('ccontact-list', counsellorViews.ContactUsList.as_view(), name='ccontact-list'), 
    path('ccontact-list/<pk>/', counsellorViews.ContactUsDetailView.as_view(), name='ccontact-detail'),
    path('cupdate/<pk>', counsellorViews.ContactUsUpdateView.as_view(), name='cupdate-contact'),
    path('job-application-list', counsellorViews.JobApplicationList.as_view(), name='job-application-list'),
    path('ccontact-followup', counsellorViews.ContactLeadFollowUpCreateView.as_view(), name='contact-followup'), 
    path('cdemo-st-list', counsellorViews.BookDemoListView.as_view(), name="cdemo-st-list")


    # Trainer Views


    # Student Views



]
