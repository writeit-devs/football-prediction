from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Blog)
admin.site.register(FreemiumProfile)
admin.site.register(PremiumProfile)
admin.site.register(League)
admin.site.register(Prediction)


