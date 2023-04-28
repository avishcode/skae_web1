from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .forms import ContactForm, AddContactFollowupForm
from crm.models import ContactUs, JoinUs, ContactLeadFollowUp
from classroom.models import BookDemo
# Create your views here.


# class ModelListView(ListView):
#     model = BookDemo
#     template_name = "crm/book_demo_list.html"


class ContactUsList(ListView):
    model = ContactUs
    template_name = "crm/admin/contact_list.html"

class ContactUsDetailView(DetailView):
    model = ContactUs
    template_name = "crm/admin/contact_detail.html"


class ContactUsUpdateView(UpdateView):
    model = ContactUs
    form_class = ContactForm
    template_name = "crm/admin/update_contact.html"
    success_url = "/contact-list"
    
class BookDemoListView(ListView):
    model = BookDemo
    template_name = "crm/admin/book_demo_list.html"

    

class JobApplicationList(ListView):
    model = JoinUs
    
    template_name = "crm/admin/job_application_list.html"


# def ContactUsList(request):
#     return render(request, "crm/contact_list.html")    




class ContactLeadFollowUpCreateView(CreateView):
    model = ContactLeadFollowUp
    form_class = AddContactFollowupForm
    template_name = "crm/admin/add_contact_followup.html"
    success_url = "/contact-list"



    