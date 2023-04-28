from django.db import models

# Create your models here.

BILLING_CYCLE = (
    ('#1', 'Daily'),
    ('#2', 'Weekly'),
    ('#3', 'Monthly'),
)

class Plan(models.Model):
    plan_name = models.CharField(max_length=200)
    plan_des = models.TextField()
    billing_fre = models.CharField(max_length=25, help_text="Billing Cycle", choices=BILLING_CYCLE)
    per_class = models.PositiveIntegerField()



class Subscription(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField()
    total_count = models.PositiveIntegerField(help_text="No. of Billing cycle to be charged")
    offer = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.username
