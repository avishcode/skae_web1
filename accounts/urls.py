from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [

    path('login/', views.login_attempt , name="login"),
    path('register/', views.register, name='register' ),
    path('otp/', views.otp, name='otp'),
    path('login-otp', views.login_otp , name="login_otp"),
    path('logout/', views.user_logout, name='logout'),
    path('student_profile', views.student_profile, name='student_profile'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('counsellor_profile', views.counsellor_profile, name='counsellor_profile'),
    path('trainer_profile', views.trainer_profile, name='trainer_profile'),
    path('account_created', views.account_created, name='account_created'),
    path('student-list', views.StudentListView.as_view(), name='student-list'),
    path('trainer-list', views.TrainerListView.as_view(), name="trainer-list"),
    path('counsellor-list', views.CounsellorListView.as_view(), name="counsellor-list"),
    path('not-authorized', views.not_authorized, name="not-authorized"),
    
]
