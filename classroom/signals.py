from classroom.models import BookDemo
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

@receiver(m2m_changed, sender=BookDemo)
def add_student_for_demo(sender, instance, action, *args, **kwargs):
    print('action', action)

