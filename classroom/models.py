from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models
from multiselectfield import MultiSelectField
from django.shortcuts import reverse
from django.utils.text import slugify
from .utils import generate_classroom_id

from accounts.models import Student, Trainer
# Create your models here.


DAYS = (
    ('#1','Sunday'),
    ('#2', 'Monday'),
    ('#3', 'Tuesday'),
    ('#4', 'Wednesday'),
    ('#5', 'Thursday'),
    ('#6', 'Friday'),
    ('#7', 'Saturday')
)


class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    note = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.start_time.strftime('%I:%M %p')} to {self.end_time.strftime('%I:%M %p')}"

class AgeGroup(models.Model):
    age_group = models.CharField(max_length=50)
    note = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.age_group)

    def get_absolute_url(self):
        return reverse("classroom:update-age-group", kwargs={"pk": self.pk})
    
    

DEMO_STATUS = (
    ('#1', 'Booked'),
    ('#2', 'Attended'),
    ('#3', 'Enrolled'),
    ('#4', 'Not Interested'),
)


class BookDemo(models.Model):
    application_id = models.CharField(max_length=40, blank=True, null=True)
    status = models.CharField(max_length=200, choices=DEMO_STATUS, default='Booked', blank= True, null=True)
    name = models.CharField(max_length=200)
    phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    phone = models.CharField(max_length=12, validators=[phone_regex], blank = True, null=True)  # you can set it unique = Truephone = models.IntegerField()
    age_group = models.ForeignKey(AgeGroup, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True)
    time = models.ForeignKey(TimeSlot, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name} - {self.age_group} - {self.date}-{self.time}"

    def get_absolute_url(self):
        return reverse("classroom:demo-detail", kwargs={"pk": self.pk})
            
    

class ClassRoomType(models.Model):
    name = models.CharField(max_length=200, null=True)
    participants = models.CharField(max_length=10)
    is_active  = models.BooleanField(default=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.description}"
    

class ClassRoom(models.Model):
    slug = models.SlugField(blank=True)
    classroom_id = models.CharField(max_length=15, blank=True)
    class_type = models.ForeignKey(ClassRoomType, on_delete=models.DO_NOTHING, null=True)
    class_room_name = models.CharField(max_length=100)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    no_of_rooms = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    # def save(self, *args, **kwargs):
    #     if self.classroom_id == "":
    #         self.classroom_id = generate_classroom_id()
    #     return super().save(*args, **kwargs)


    def save(self, *args, **kwargs):
        if self.classroom_id == "":
            self.classroom_id = generate_classroom_id()
        self.slug = slugify(self.class_room_name)
        super(ClassRoom, self).save(*args, **kwargs)

    def __str__(self):
        return self.class_room_name

    def get_absolute_url(self):
        return reverse("classroom:classroom-detail", kwargs={"slug": self.slug})
    
    @property
    def rooms(self):
        return self.room_set.all().order_by('position')




ROOM_STATUS = (
    ('#1', 'Active'),
    ('#2', 'Inactive'),
    ('#3', 'Removed'),
)


class Room(models.Model):
    slug = models.SlugField(blank=True, null=True)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.DO_NOTHING)
    position = models.IntegerField(blank=True, null=True)
    room_status = models.CharField(max_length=30, choices=ROOM_STATUS, default="#1")
    room_id = models.CharField(max_length=20, null=True)
    room_name = models.CharField(max_length=200, null=True)
    days = MultiSelectField(choices=DAYS, max_length=10)
    trainer = models.ForeignKey(Trainer, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.room_name)
        super(Room, self).save(*args, **kwargs)

    def __str__(self):
        return self.room_name

    def get_absolute_url(self):
        return reverse("classroom:room-detail", 
        kwargs={
            "classroom_slug": self.classroom.slug,
            "room_slug": self.slug
            }
        )
            



EXPRESSION_CHOICE = (
    ('Y', 'Yes'),
    ('N', 'No')
)

""""
class DemoClassFeedBack(models.Model):
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    trainer = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)],
                                  help_text="How was your experience with Trainer")
    topic = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)],
                                help_text="Did you enjoy today's topic")
    technical = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)],
                                    help_text="How was audio and video quality")
    expression = models.CharField(max_length=3, choices=EXPRESSION_CHOICE, blank=True,
                                  help_text="Did you were able to express your word and "
                                            "topic")


class ClassStudentFeedBack(models.Model):
    classroom_id = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    student = models.CharField(max_length=100, blank=True, help_text="list of student")
    trainer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    pronunciation = models.IntegerField(blank=True)
    grammar_expression = models.IntegerField(blank=True)
    confidence = models.IntegerField(blank=True)
    fluency = models.IntegerField(blank=True)
    content = models.IntegerField(blank=True)
    watch_time = models.TimeField(auto_now_add=True)
    notes = models.CharField(max_length=100, blank=True)


class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    # session_year_id = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class AttendanceReport(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

"""
class ClassRoomAttendance(models.Model):
    st_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    clsrm = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    login_in = models.TimeField(auto_now_add=True)
    log_out = models.TimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.st_id} - {self.login_in} - {self.log_out}"
    