from django.db import models
from django.db.models.deletion import SET_NULL
from accounts.models import Student
from classroom.models import AgeGroup
from django.utils.text import slugify
from fee.models import Plan, Subscription

# Create your models here.


class MembershipType(models.Model):
    slug = models.SlugField(blank=True)
    name = models.CharField(max_length=200)
    age_group = models.ForeignKey(AgeGroup, on_delete=models.SET_NULL, null=True)
    no_of_participants = models.IntegerField()
    no_of_classes = models.IntegerField()
    shot_des = models.CharField(max_length=200)
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(MembershipType, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    


# class MembershipFeatures(models.Model):
#     mem_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE)


class Membership(models.Model):
    slug = models.SlugField(blank=True)
    mem_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    plan = models.ForeignKey(Plan, on_delete=SET_NULL, null=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Membership, self).save(*args, **kwargs)


    def __str__(self):
        return self.name
    



class UserMembership(models.Model):
    user = models.OneToOneField(
        Student, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=40)
    membership = models.ForeignKey(
        Membership, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username    



