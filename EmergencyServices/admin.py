from django.contrib import admin
from .models import PoliceEmergency, HealthEmergency, HealthTest

admin.site.register(HealthEmergency)
admin.site.register(PoliceEmergency)
admin.site.register(HealthTest)


# Register your models here.
