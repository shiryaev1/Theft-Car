from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from announcement.models import Announcement


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=300, blank=True)
    born = models.DateField(null=True, blank=True)
    email = models.EmailField()
    image = models.ImageField(upload_to='media/user_image', default='')
    # announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
#
#
#
# @receiver(post_save, sender=User)
# def new_user(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()