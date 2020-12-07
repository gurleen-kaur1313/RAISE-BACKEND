from django.conf import settings
from django.db import models
import uuid


class PoliceEmergency(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    longitude = models.CharField(null=True,blank=True,max_length=250)
    latitude = models.CharField(null=True,blank=True, max_length=250)
    date = models.CharField(null=True,blank=True, max_length=250)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        super(PoliceEmergency, self).save(*args, **kwargs)


class HealthEmergency(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    problem = models.TextField(help_text="Problem : ")
    longitude = models.CharField(null=True,blank=True,max_length=250)
    latitude = models.CharField(null=True,blank=True,max_length=250)
    date = models.CharField(null=True,blank=True, max_length=250)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        super(HealthEmergency, self).save(*args, **kwargs)


class UnsafeAreas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.CharField(null=True,blank=True,max_length=250)
    state = models.CharField(null=True,blank=True,max_length=250)
    flag = models.IntegerField(null=True,blank=True,default=0)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city

    def save(self, *args, **kwargs):
        super(UnsafeAreas, self).save(*args, **kwargs)




class HealthTest(models.Model):
    TEST_CHOICES = (
        ("covid_symptoms", "Covid-19 Symptoms"),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    test = models.CharField(
        max_length=250, choices=TEST_CHOICES, blank=True, null=True
    )
    date = models.DateTimeField(auto_now_add=True)
    remarksDoc = models.CharField(null=True, blank=True, max_length=255)
    remarksPat = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        super(HealthTest, self).save(*args, **kwargs)


class Jobs(models.Model):
    title = models.CharField(blank=True, max_length=250,null=False)
    description = models.TextField(null=True,blank=True)
    pay = models.IntegerField(null=True,blank=True)
    skillsrequired = models.TextField(null=True,blank=True)
    mobile=models.CharField(blank=True,null=True,max_length=16)
    location=models.CharField(blank=True,null=True,max_length=250)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Jobs, self).save(*args, **kwargs)
