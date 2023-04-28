from django.db import models

# Create your models here.


class StudentTestimonials(models.Model):
    profile = models.FileField(blank=True, upload_to='testimonials')
    name = models.CharField(max_length=200)
    batch = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    company_logo = models.ImageField(blank=True, upload_to='company_logo')
    com_post = models.CharField(max_length=100)

    def __str__(self):
        return f"name:{self.name}, batch: {self.batch}"
    


class DirectorMessage(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    image = models.FileField(blank=True, upload_to='web/img')
    description = models.TextField()
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return f"name{self.name}, description: {self.description}"
    


class TeamMembers(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(blank=True, upload_to='web/team_members')
    profile = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"name{self.name}, description: {self.description}"
        
class HomePageFAQ(models.Model):
    question = models.CharField(max_length=200)        
    answer = models.TextField()

    def __str__(self):
        return f"Question: {self.question}, answer: {self.answer}"


class BookDemoPage(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    image = models.FileField(upload_to='web/book_demo')

    def __str__(self):
        return self.title
    

class CareerPage(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    image = models.FileField(upload_to='web/career')

    def __str__(self):
        return self.title

class ContactUsPage(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    image = models.FileField(upload_to='web/career')

    def __str__(self):
        return self.title
