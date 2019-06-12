from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.urls import reverse

class PersonProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)

    adress=models.CharField(max_length=100,default='', blank=True)
    
    phone=models.CharField(max_length=20,default='', blank=True)
    description=models.TextField(default='',blank=True)
    
    image = models.FileField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    spec=models.IntegerField(default=0) #0 - deg, 1 - mus, 2 - org

    #humans only
    birth_date=models.CharField(max_length=100, default='', blank=True)
    #mus
    nickname=models.CharField(max_length=100,default='', blank=True)
    genres=models.CharField(max_length=100,default='', blank=True)
    instruments=models.CharField(max_length=200,default='', blank=True)
    soundcloud=models.CharField(max_length=100, default='', blank=True)
    #org
    company=models.CharField(max_length=100,default='', blank=True)

    followers = models.ManyToManyField('self', related_name='follows', symmetrical=False) 
    # group = models.ManyToManyField(GroupProfile, related_name='users', symmetrical=False)
    

    User.profile = property(lambda u: PersonProfile.objects.get_or_create(user=u)[0])

class GroupProfile(models.Model):
    name = models.CharField(max_length=100,default='', blank=False)
    #users = models.ManyToManyField(PersonProfile)
    description=models.TextField(default='',blank=True)
    genres=models.CharField(max_length=100,default='', blank=True)
    instruments=models.CharField(max_length=200,default='', blank=True)
    soundcloud=models.CharField(max_length=100, default='', blank=True)
    create_date = models.CharField(max_length=100, default='', blank=True)
    image = models.FileField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

    def get_absolute_url(self):
        return reverse('groupprofile-detail', kwargs={'pk': self.pk})
    

class EventProfile(models.Model):
    name = models.CharField(max_length=100,default='', blank=False)
    address = models.CharField(max_length=100,default='', blank=False)
    date = models.CharField(max_length=100, default='', blank=False)
    description = models.TextField(default='',blank=True) 
    company = models.ForeignKey(PersonProfile, on_delete=models.CASCADE, blank=False)

    #self.info = (name, date, address, group)

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})

    def get_event_info(self):
        return(self.info)

class AcceptedEvent(models.Model):
    user = models.ForeignKey(PersonProfile, on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey(GroupProfile, on_delete=models.CASCADE, blank=True, null=True)
    event = models.ForeignKey(EventProfile, on_delete=models.CASCADE, blank=False)
    accepted = models.BooleanField(blank=False, default=False)

class AcceptedGroup(models.Model):
    user = models.ForeignKey(PersonProfile, on_delete=models.CASCADE, blank=True)
    group = models.ForeignKey(GroupProfile, on_delete=models.CASCADE)
    accepted = models.BooleanField(blank=False, default=False)


class Participation(models.Model):
    userProfile = models.ForeignKey(PersonProfile, on_delete=models.CASCADE, blank=False)
    is_mus=models.BooleanField(blank=False, default=False) #Участвует в мероприятии как музыкант или нет
    event = models.ForeignKey(EventProfile, on_delete=models.CASCADE, blank=False)

class RequestEvent(models.Model):
    users = models.ManyToManyField(PersonProfile)
    groups = models.ManyToManyField(GroupProfile) 
    event = models.ForeignKey(EventProfile, on_delete=models.CASCADE, blank=False)
    seen = models.BooleanField(blank=False, default=False) 
    accepted = models.BooleanField(blank=False, default=False) 
    declined = models.BooleanField(blank=False, default=False)

class RequestGroup(models.Model):
    users = models.ManyToManyField(PersonProfile)
    group = models.ForeignKey(GroupProfile, on_delete=models.CASCADE, blank=False)
    seen = models.BooleanField(blank=False, default=False) 
    accepted = models.BooleanField(blank=False, default=False) 
    declined = models.BooleanField(blank=False, default=False)


#сигналы
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        PersonProfile.objects.create(user=instance)
        # MusicianProfile.objects.create(user=instance)
        # CompanyProfile.objects.create(user=instance)
        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    # instance.MusicianProfile.save()
    # instance.CompanyProfile.save()



# class MusicianProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
#     adress=models.CharField(max_length=100,default='', blank=False)
#     birth_date=models.DateField(default=timezone.now(), blank=False)
#     phone=models.CharField(max_length=20,default='', blank=True)

#     nickname=models.CharField(max_length=100,default='')
#     genres=models.CharField(max_length=100,default='')
#     instruments=models.CharField(max_length=200,default='')
#     soundcloud=models.URLField(default='/', blank=True)

#     description=models.TextField(default='',blank=True)
#     image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
#     User.profile = property(lambda u: MusicianProfile.objects.get_or_create(user=u)[0])



# class CompanyProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     adress=models.CharField(max_length=100,default='')
#     phone=models.CharField(max_length=20,default='')

#     company=models.CharField(max_length=100,default='')

#     description=models.TextField(default='',blank=True)
#     image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
#     User.profile = property(lambda u: CompanyProfile.objects.get_or_create(user=u)[0])





