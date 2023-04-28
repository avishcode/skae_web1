from django.urls import path

from website import views

app_name = 'website'

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('course', views.Courses, name='course'),
    path('course-detail-page',views.CourseDetailPage, name='course-detail-page'),
    path('about-us', views.AboutUs, name='about-us'),
    path('book-demo-page', views.BookDemoPage.as_view(), name='book-demo-page'),
    path('career', views.Career, name='career'),
    path('contact-us', views.ContactUs.as_view(), name='contact-us'),
    path('checkout', views.checkout, name='checkout'),
    path('thanks', views.ThankYou.as_view(), name='thanks'),
]
