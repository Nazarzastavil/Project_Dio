from django.db import models

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    registertime=models.DateField()
    date=models.DateField()
    name=models.CharField(max_length=200)
    spec=models.IntegerField
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    description=models.TextField()
    image = models.FileField(null=True, blank=True)


    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/%s/" %(self.id)

class Meta:
    ordering = ["-id", "-registertime"]
