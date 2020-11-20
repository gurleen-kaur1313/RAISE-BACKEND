from django.conf import settings
from django.db import models


class PoliceEmergency(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        super(PoliceEmergency, self).save(*args, **kwargs)


class HealthEmergency(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    problem = models.TextField(help_text="Problem : ")
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        super(HealthEmergency, self).save(*args, **kwargs)


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


# Create your models here.
