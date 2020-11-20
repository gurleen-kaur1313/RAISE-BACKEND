from django.contrib import admin
from .models import User, Profile, PeriodTracker, Exercise

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(PeriodTracker)
admin.site.register(Exercise)
