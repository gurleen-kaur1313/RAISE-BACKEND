from django.contrib import admin
from .models import PoliceEmergency, HealthEmergency, HealthTest, Jobs, UnsafeAreas

admin.site.register(HealthEmergency)
admin.site.register(PoliceEmergency)
admin.site.register(HealthTest)
admin.site.register(Jobs)
admin.site.register(UnsafeAreas)

# Register your models here.
