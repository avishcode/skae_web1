from django.urls import path
from reports import views
app_name = 'reports'

urlpatterns = [
    path('demo', views.demo, name='demo'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('trainer_dashboard', views.trainer_dashboard, name='trainer_dashboard'),
    path('student_dashboard', views.student_dashboard, name='student_dashboard'),
    path('counsellor_dashboard', views.counsellor_dashboard, name='counsellor_dashboard'),
    path('enorllment-stats', views.EnrollmentStatstics.as_view(), name='enorllment-stats'),
    path('payment-received', views.PaymentReceived.as_view(), name='payment-received'),
    path('promo-code-stats', views.PromoCodeStatstics.as_view(), name='promo-code-stats'),
    path('refferal-stats', views.RefferalReports.as_view(), name='refferal-stats'),
    path('trainer-list/', views.TrainerList, name='trainer-list'),
    path('counsellor-list/', views.CounsellorList, name='counsellor-list'),
    path('student-list/', views.StudentList, name='student-list'),
    path('setting', views.setting, name="setting"),
    path('sidebar', views.sidebar, name='sidebar'),

]
