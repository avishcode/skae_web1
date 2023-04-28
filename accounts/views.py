import random

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView
# Create your views here.
from accounts.decorators import unauthenticated_user, allowed_users
from accounts.models import Counsellor, PhoneVerify, Student, Trainer
import http.client


def demo(request):
    return render(request, 'demo.html')


def send_otp(mobile, otp):
    print(otp)
    conn = http.client.HTTPConnection("2factor.in")
    # authkey = settings.AUTH_KEY
    headers = {'content-type': "application/json"}
    conn.request("GET",
                 "https://2factor.in/API/R1/?module=SMS_OTP&apikey=fb3df403-12c4-11eb-9fa5-0200cd936042&to=" + mobile + "&otpvalue=" + str() + "&templatename=WomenMark1")
    res = conn.getresponse()
    data = res.read()
    print(data)
    return None


@unauthenticated_user
def login_attempt(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')

        user = PhoneVerify.objects.filter(mobile=mobile).first()

        if user is None:
            context = {'message': 'User not found', 'class': 'danger'}
            return render(request, 'accounts/login.html', context)

        otp = str(random.randint(1000, 9999))
        user.otp = otp
        user.save()
        send_otp(mobile, otp)
        request.session['mobile'] = mobile
        return redirect('accounts:login_otp')
    return render(request, 'accounts/login.html')


def login_otp(request):
    mobile = request.session['mobile']
    context = {'mobile': mobile}
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = PhoneVerify.objects.filter(mobile=mobile).first()

        if otp == profile.otp:
            user = User.objects.get(id=profile.user.id)
            login(request, user)
            return redirect('reports:admin_dashboard')
        else:
            context = {'message': 'Wrong OTP', 'class': 'danger', 'mobile': mobile}
            return render(request, 'accounts/login_otp.html', context)

    return render(request, 'accounts/login_otp.html', context)


def user_login(request):
    return render(request, "accounts/login.html")


@unauthenticated_user
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')

        check_user = User.objects.filter(email=email).first()
        check_profile = PhoneVerify.objects.filter(mobile=mobile).first()

        if check_user or check_profile:
            context = {'message': 'User already exists', 'class': 'danger'}
            return render(request, 'accounts/register.html', context)

        user = User(email=email, username=name)
        user.save()
        group = Group.objects.get(name='student')
        user.groups.add(group)

        otp = str(random.randint(1000, 9999))
        profile = PhoneVerify(user=user, mobile=mobile, otp=otp)
        profile.save()
        send_otp(mobile, otp)
        request.session['mobile'] = mobile
        return redirect('/otp/')
    return render(request, 'accounts/register.html')


def otp(request):
    mobile = request.session['mobile']
    context = {'mobile': mobile}
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = PhoneVerify.objects.filter(mobile=mobile).first()

        if otp == profile.otp:
            return redirect('accounts:login')
        else:
            print('Wrong')

            context = {'message': 'Wrong OTP', 'class': 'danger', 'mobile': mobile}
            return render(request, 'accounts/otp.html', context)
    return render(request, "accounts/otp.html", context)


# ye abhi kisi kaam ka nahi hai
# def user_profile(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             fm = EditUserProfileForm(request.POST, instance=request.user)
#             if fm.is_valid():
#                 messages.success(request, 'Profile Updated Successfully')
#                 fm.save()
#         else:
#             fm = EditUserProfileForm(instance=request.user)
#         return render(request, 'accounts/user_profile.html', {'name': request.user, 'form': fm})
#     else:
#         return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
@allowed_users(allowed_roles=['admin','counsellor','trainer'])


@login_required(login_url="/accounts:login/")
def student_profile(request):
    return render(request, "accounts/student_profile.html", {'username': request.user})


@allowed_users(allowed_roles=['admin'])
def admin_profile(request):
    if request.user.is_authenticated:
        return render(request, "accounts/admin_profile.html", {'username': request.user})
    else:
        return HttpResponseRedirect('accounts:login')

@login_required(login_url="/accounts:login/")
@allowed_users(allowed_roles=['admin', 'counsellor', 'trainer'])
def trainer_profile(request):
    if request.user.is_authenticated:
        return render(request, "accounts/trainer_profile.html", {'username': request.user})
    else:
        return HttpResponseRedirect('accounts:login')

@login_required(login_url="/accounts:login/")
@allowed_users(allowed_roles=['admin', 'counsellor'])
def counsellor_profile(request):
    if request.user.is_authenticated:
        return render(request, "accounts/counsellor_profile.html", {'username': request.user})
    else:
        return HttpResponseRedirect('login')


def account_created(request):
    return render(request, "accounts/account_created-confirmation.html")







class StudentListView(ListView):
    model = Student
    template_name = "accounts/student_list.html"


class TrainerListView(ListView):
    model = Trainer
    template_name = "accounts/trainer_list.html"


class CounsellorListView(ListView):
    model = Counsellor
    template_name = "accounts/counsellor_list.html"        


def not_authorized(request):
    return render(request, "accounts/403.html")