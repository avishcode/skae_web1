from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from .forms import ContactUsForm
from classroom.forms import BookDemoForm
from django.views.generic.base import TemplateView
from crm.models import JoinUs


def HomePage(request):
    context = {}
    return render(request, "website/homepage.html", context)


def AboutUs(request):
    context={}
    return render(request, "website/about_us.html")

def Courses(request):
    context = {}
    return render(request, "website/courses_display.html")    

   

class BookDemoPage(CreateView):
    form_class = BookDemoForm
    template_name = "website/book_demo_page.html"
    success_url = 'thanks'    

class ContactUs(CreateView):
    form_class = ContactUsForm
    template_name = "website/contact_us.html"
    success_url = 'thanks'   


def Career(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        median_name = request.POST.get('median_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        education = request.POST.get('education')
        working_exp = request.POST.get('working_exp')
        hobbies = request.POST.get('hobbies')
        strength = request.POST.get('strength')
        weakness = request.POST.get('weakness')
        skills = request.POST.get('skills')
        discussion_topic = request.POST.get('discussion_topic')
        describe_life = request.POST.get('describe_life')
        describe_yourself = request.POST.get('describe_yourself')
        non_judgmental = request.POST.get('non_judgmental')
        counselling = request.POST.get('counselling')
        resume = request.FILES['resume']

        jobapln = JoinUs(first_name=first_name, median_name=median_name, last_name=last_name, email=email, phone=phone, dob=dob, address=address, city=city, state=state, education=education, working_exp=working_exp, hobbies=hobbies, strength=strength, weakness=weakness, skills=skills, discussion_topic=discussion_topic, describe_life=describe_life, describe_yourself=describe_yourself, non_judgmental=non_judgmental, counselling=counselling, resume=resume)

        print("Form submitted Successfully")
        return redirect("website:thanks")
        jobapln.save()
    context = {}
    return render(request, "website/job_application_form.html")
    
def checkout(request):
    context = {}
    return render(request, "website/checkout.html")

def CourseDetailPage(request):
    context = {}
    return render(request, "website/course_detail_page.html")



class ThankYou(TemplateView):
    template_name = "website/thank_you.html"     