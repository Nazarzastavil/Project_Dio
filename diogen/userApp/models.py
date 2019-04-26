from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class PersonProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #name=models.CharField(max_length=200, blank=False)
    
    birth_date=models.DateField(default='1999-01-01')
    spec=models.IntegerField(default=0)
    phone=models.CharField(max_length=20,default='test')
    description=models.TextField(default='test')
    image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')


User.profile = property(lambda u: PersonProfile.objects.get_or_create(user=u)[0])

#сигналы
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        PersonProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()