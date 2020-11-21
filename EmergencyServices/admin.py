from django.contrib import admin
from .models import PoliceEmergency, HealthEmergency, HealthTest, Jobs

admin.site.register(HealthEmergency)
admin.site.register(PoliceEmergency)
admin.site.register(HealthTest)
admin.site.register(Jobs)

# Register your models here.
