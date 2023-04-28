from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.shortcuts import reverse
from accounts.models import Counsellor
from classroom.models import BookDemo, DEMO_STATUS
# Create your models here.


class DemoStudentFollowUp(models.Model):
    demo_st = models.ForeignKey(BookDemo, on_delete=models.CASCADE)
    owner = models.ForeignKey(Counsellor, on_delete=models.SET_NULL, null=True)
    
    note = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False)



class JobCategory(models.Model):
    job_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=250, blank=True, help_text="short description about the job")
    status = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_name} - {self.desc} - {self.created.strftime('%d/%m/%Y')}"




class JobDetail(models.Model):
    job_cat = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    job_desc = models.TextField(max_length=300)
    skill = models.CharField(max_length=300)
    roles_responsibilty = models.CharField(max_length=300)
    video_url = models.URLField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_cat}-{self.created.strftime('%d/%m/%Y')}"
    
    



# form will be submitted in 3 step(
# 1 > Personal Details
# 2 > Academic and work expreince
# 3 > Views and Opnions)

APPLICATION_STATUS = (
    ('Applied', 'Applied'),
    ('Scheduled', 'Scheduled'),
    ('Selected', 'Selected'),
    ('Rejected', 'Rejected'),
)


STATE_CHOICES = (
  ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
  ('Andhra Pradesh','Andhra Pradesh'),
  ('Arunachal Pradesh','Arunachal Pradesh'),
  ('Assam','Assam'),
  ('Bihar','Bihar'),
  ('Chandigarh','Chandigarh'),
  ('Chhattisgarh','Chhattisgarh'),
  ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
  ('Daman and Diu','Daman and Diu'),
  ('Delhi','Delhi'),
  ('Goa','Goa'),
  ('Gujarat','Gujarat'),
  ('Haryana','Haryana'),
  ('Himachal Pradesh','Himachal Pradesh'),
  ('Jammu & Kashmir','Jammu & Kashmir'),
  ('Jharkhand','Jharkhand'),
  ('Karnataka','Karnataka'),
  ('Kerala','Kerala'),
  ('Lakshadweep','Lakshadweep'),
  ('Madhya Pradesh','Madhya Pradesh'),
  ('Maharashtra','Maharashtra'),
  ('Manipur','Manipur'),
  ('Meghalaya','Meghalaya'),
  ('Mizoram','Mizoram'),
  ('Nagaland','Nagaland'),
  ('Odisha','Odisha'),
  ('Puducherry','Puducherry'),
  ('Punjab','Punjab'),
  ('Rajasthan','Rajasthan'),
  ('Sikkim','Sikkim'),
  ('Tamil Nadu','Tamil Nadu'),
  ('Telangana','Telangana'),
  ('Tripura','Tripura'),
  ('Uttarakhand','Uttarakhand'),
  ('Uttar Pradesh','Uttar Pradesh'),
  ('West Bengal','West Bengal'),
)

class JoinUs(models.Model):
    application_id = models.CharField(max_length=15, blank=True)
    status = models.CharField(max_length=20, choices=APPLICATION_STATUS, default='Applied')
    job_cat = models.ForeignKey(JobCategory, on_delete=models.DO_NOTHING, blank=True, null=True)
    first_name = models.CharField(max_length=200, null=True)
    median_name = models.CharField(max_length=200, blank=True,null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    phone = models.CharField(max_length=255, validators=[phone_regex], null=True)
    dob = models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    education = models.CharField(max_length=100)
    working_exp = models.TextField()
    hobbies = models.TextField()
    strength = models.TextField()
    weakness = models.TextField()
    skills = models.TextField()
    discussion_topic = models.TextField(help_text='5 favorite topic for discussion')
    describe_life = models.TextField(help_text='Your Opinion about life')
    describe_yourself = models.TextField(help_text='Describe Yourself')
    non_judgmental = models.TextField(help_text='What do you mean by non-jugmental')
    counselling = models.TextField(help_text='What do you mean by counselling')
    resume = models.FileField(upload_to='Resume', null=True)



QUERY_STATUS = (
    ('Pending', 'Pending'),
    ('Resolved', 'Resolved'),
    ('Hold', 'Hold'),
)

class ContactUs(models.Model):
    query_id = models.CharField(max_length=15, blank=True)
    query_status = models.CharField(max_length=20, choices=QUERY_STATUS, default='Pending')
    name = models.CharField(max_length=150)
    phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    phone = models.CharField(max_length=255, validators=[phone_regex], blank = True, null=True)  # you can set it unique = Truephone = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()
    follow_up_note = models.CharField(max_length=200, null=True)
    owner = models.ForeignKey(Counsellor, on_delete=models.DO_NOTHING, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.created.strftime('%d/%m/%Y')}"


    def get_absolute_url(self):
        return reverse("crm:contact-detail", kwargs={"pk": self.pk})        


class ContactLeadFollowUp(models.Model):
    query_status = models.CharField(max_length=20, choices=QUERY_STATUS, default='Pending')
    contact = models.ForeignKey(ContactUs, on_delete=models.CASCADE)
    owner = models.ForeignKey(Counsellor, on_delete=models.DO_NOTHING, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    note = models.CharField(max_length=200)
    next_followup_date = models.DateField(blank=True, null=True)
    next_followup_time = models.TimeField(blank=True, null=True)
    
    def __str__(self):
        return self.note
    



    