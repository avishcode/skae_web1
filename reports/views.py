from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from accounts.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required

# Create your views here.

def demo(request):
    return render(request, "reports/admin/demo_page2.html")

@admin_only
def admin_dashboard(request):
    if request.user.is_authenticated:
        context = {'username':request.user}
        return render(request, "reports/admin/admin_dashboard.html", context)



@login_required(login_url="/login/")
@allowed_users(allowed_roles=['admin', 'counsellor', 'trainer'])
def trainer_dashboard(request):
    if request.user.is_authenticated:
        context = {'username':request.user}
        return render(request, "reports/trainer/tr_dashboard.html",context)


@login_required(login_url="/login/")
@allowed_users(allowed_roles=['admin', 'counsellor'])
def counsellor_dashboard(request):
    if request.user.is_authenticated:
        context = {'username':request.user}
        return render(request,"reports/counsellor/counsellor_dashboard.html", context)


@login_required(login_url="/login/")
@allowed_users(allowed_roles=['admin', 'counsellor', 'student'])
def student_dashboard(request):
     if request.user.is_authenticated:
         context = {'username':request.user}
         return render(request, "reports/student/st_dashboard.html", context)



class PaymentReceived(TemplateView):
    template_name = "reports/admin/payment_received.html"

class EnrollmentStatstics(TemplateView):
    template_name = "reports/admin/enrollment_stastics.html"    

class PromoCodeStatstics(TemplateView):
    template_name = "reports/admin/promo_code_stats.html"    

class RefferalReports(TemplateView):
    template_name = "reports/admin/refferal_report.html"    


def TrainerList(request):
    return render(request,"accounts/trainer_list.html")

def StudentList(request):
    return render(request, "accounts/student_list.html")    

def CounsellorList(request):
    return render(request, "accounts/counsellor_list.html")    

def AdminProfile(request):
    return render(request, "accounts/admin_profile.html")


def sidebar(request):
    return render(request, "reports/sidebar2.html") 


def setting(request):
    return render(request, "reports/admin/setting.html")    


