from django.contrib import admin
from .models import UserComplaintForm, UserProfile, NewIDApplicationModelForm, StatusCorrectionModelForm, LostIDReapplicationModelForm

# Register your models here.

admin.site.register(UserComplaintForm)
admin.site.register(UserProfile)
admin.site.register(NewIDApplicationModelForm)
admin.site.register(StatusCorrectionModelForm)
admin.site.register(LostIDReapplicationModelForm)