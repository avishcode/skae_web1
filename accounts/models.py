from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator, MaxLengthValidator
# Create your models here.
from django.urls import reverse


class SessionYearModel(models.Model):
    id = models.AutoField(primary_key=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    object = models.Manager()


class PhoneVerify(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    mobile = models.CharField(max_length=255, validators=[validators.MaxLengthValidator(10)], blank = True, null=True)  # you can set it unique = Truephone = models.IntegerField()
    otp = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.user} - {self.mobile}"


class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.ForeignKey(PhoneVerify, on_delete=models.DO_NOTHING, null=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    qualification = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.admin} - {self.phone.mobile}"


class Student(models.Model):
    st_id = models.AutoField(primary_key=True)
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.ForeignKey(PhoneVerify, on_delete=models.DO_NOTHING, null=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    qualification = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='stu_profile')
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.phone.mobile}"


# def create_student(sender, instance, created, **kwarg):
#     if created:
#         Student.objects.create(user=instance)
#         print('Student Created')


# post_save.connect(create_student, sender=User)

class Trainer(models.Model):
    tr_id = models.AutoField(primary_key=True)
    trainer = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.ForeignKey(PhoneVerify, on_delete=models.DO_NOTHING, null=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    qualification = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.trainer} - {self.phone.mobile}"

    # def get_absolute_url(self):
    #     return reverse("trainer-list")


class Counsellor(models.Model):
    cnl_id = models.AutoField(primary_key=True)
    counsellor = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.ForeignKey(PhoneVerify, on_delete=models.DO_NOTHING, null=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    qualification = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.counsellor}"